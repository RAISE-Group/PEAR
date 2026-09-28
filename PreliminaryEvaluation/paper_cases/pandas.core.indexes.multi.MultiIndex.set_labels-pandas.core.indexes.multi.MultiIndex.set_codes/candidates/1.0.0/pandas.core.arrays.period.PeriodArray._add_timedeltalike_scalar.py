def _add_timedeltalike_scalar(self, other):
    """
        Parameters
        ----------
        other : timedelta, Tick, np.timedelta64

        Returns
        -------
        result : ndarray[int64]
        """
    assert isinstance(self.freq, Tick)
    assert isinstance(other, (timedelta, np.timedelta64, Tick))
    if notna(other):
        other = self._check_timedeltalike_freq_compat(other)
    ordinals = super()._add_timedeltalike_scalar(other)
    return ordinals