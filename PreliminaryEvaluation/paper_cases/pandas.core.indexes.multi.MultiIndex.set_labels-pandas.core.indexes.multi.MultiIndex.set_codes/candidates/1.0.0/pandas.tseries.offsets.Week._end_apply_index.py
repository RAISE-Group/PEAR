def _end_apply_index(self, dtindex):
    """
        Add self to the given DatetimeIndex, specialized for case where
        self.weekday is non-null.

        Parameters
        ----------
        dtindex : DatetimeIndex

        Returns
        -------
        result : DatetimeIndex
        """
    off = dtindex.to_perioddelta('D')
    base, mult = libfrequencies.get_freq_code(self.freqstr)
    base_period = dtindex.to_period(base)
    if not isinstance(base_period._data, np.ndarray):
        base_period = base_period._data
    if self.n > 0:
        normed = dtindex - off + Timedelta(1, 'D') - Timedelta(1, 'ns')
        roll = np.where(base_period.to_timestamp(how='end') == normed, self.n, self.n - 1)
        shifted = base_period._addsub_int_array(roll, operator.add)
        base = shifted.to_timestamp(how='end')
    else:
        roll = self.n
        base = base_period._time_shift(roll).to_timestamp(how='end')
    return base + off + Timedelta(1, 'ns') - Timedelta(1, 'D')