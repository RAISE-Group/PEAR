def _get_period_bins(self, ax):
    if not isinstance(ax, PeriodIndex):
        raise TypeError(f'axis must be a PeriodIndex, but got an instance of {type(ax).__name__}')
    memb = ax.asfreq(self.freq, how=self.convention)
    nat_count = 0
    if memb.hasnans:
        nat_count = np.sum(memb._isnan)
        memb = memb[~memb._isnan]
    if not len(memb):
        binner = labels = PeriodIndex(data=[], freq=self.freq, name=ax.name)
        return (binner, [], labels)
    freq_mult = self.freq.n
    start = ax.min().asfreq(self.freq, how=self.convention)
    end = ax.max().asfreq(self.freq, how='end')
    bin_shift = 0
    if self.base:
        p_start, end = _get_period_range_edges(start, end, self.freq, closed=self.closed, base=self.base)
        start_offset = Period(start, self.freq) - Period(p_start, self.freq)
        bin_shift = start_offset.n % freq_mult
        start = p_start
    labels = binner = period_range(start=start, end=end, freq=self.freq, name=ax.name)
    i8 = memb.asi8
    expected_bins_count = len(binner) * freq_mult
    i8_extend = expected_bins_count - (i8[-1] - i8[0])
    rng = np.arange(i8[0], i8[-1] + i8_extend, freq_mult)
    rng += freq_mult
    rng -= bin_shift
    prng = type(memb._data)(rng, dtype=memb.dtype)
    bins = memb.searchsorted(prng, side='left')
    if nat_count > 0:
        bins += nat_count
        bins = np.insert(bins, 0, nat_count)
        binner = binner.insert(0, NaT)
        labels = labels.insert(0, NaT)
    return (binner, bins, labels)