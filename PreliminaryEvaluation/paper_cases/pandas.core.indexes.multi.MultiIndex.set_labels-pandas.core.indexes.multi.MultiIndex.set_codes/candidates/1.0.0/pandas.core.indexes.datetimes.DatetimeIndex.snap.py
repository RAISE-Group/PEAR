def snap(self, freq='S'):
    """
        Snap time stamps to nearest occurring frequency.

        Returns
        -------
        DatetimeIndex
        """
    freq = to_offset(freq)
    snapped = np.empty(len(self), dtype=_NS_DTYPE)
    for i, v in enumerate(self):
        s = v
        if not freq.is_on_offset(s):
            t0 = freq.rollback(s)
            t1 = freq.rollforward(s)
            if abs(s - t0) < abs(t1 - s):
                s = t0
            else:
                s = t1
        snapped[i] = s
    return DatetimeIndex._simple_new(snapped, name=self.name, tz=self.tz, freq=freq)