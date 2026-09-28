def _maybe_convert_timedelta(self, other):
    """
        Convert timedelta-like input to an integer multiple of self.freq

        Parameters
        ----------
        other : timedelta, np.timedelta64, DateOffset, int, np.ndarray

        Returns
        -------
        converted : int, np.ndarray[int64]

        Raises
        ------
        IncompatibleFrequency : if the input cannot be written as a multiple
            of self.freq.  Note IncompatibleFrequency subclasses ValueError.
        """
    if isinstance(other, (timedelta, np.timedelta64, Tick, np.ndarray)):
        offset = frequencies.to_offset(self.freq.rule_code)
        if isinstance(offset, Tick):
            delta = self._data._check_timedeltalike_freq_compat(other)
            return delta
    elif isinstance(other, DateOffset):
        freqstr = other.rule_code
        base = libfrequencies.get_base_alias(freqstr)
        if base == self.freq.rule_code:
            return other.n
        raise raise_on_incompatible(self, other)
    elif is_integer(other):
        return other
    raise raise_on_incompatible(self, None)