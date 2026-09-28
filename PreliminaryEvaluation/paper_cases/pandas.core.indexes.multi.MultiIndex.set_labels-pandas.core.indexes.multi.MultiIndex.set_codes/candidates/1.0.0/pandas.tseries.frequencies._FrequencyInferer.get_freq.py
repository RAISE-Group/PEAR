def get_freq(self) -> Optional[str]:
    """
        Find the appropriate frequency string to describe the inferred
        frequency of self.values

        Returns
        -------
        str or None
        """
    if not self.is_monotonic or not self.index._is_unique:
        return None
    delta = self.deltas[0]
    if _is_multiple(delta, _ONE_DAY):
        return self._infer_daily_rule()
    if self.hour_deltas in ([1, 17], [1, 65], [1, 17, 65]):
        return 'BH'
    elif not self.is_unique_asi8:
        return None
    delta = self.deltas_asi8[0]
    if _is_multiple(delta, _ONE_HOUR):
        return _maybe_add_count('H', delta / _ONE_HOUR)
    elif _is_multiple(delta, _ONE_MINUTE):
        return _maybe_add_count('T', delta / _ONE_MINUTE)
    elif _is_multiple(delta, _ONE_SECOND):
        return _maybe_add_count('S', delta / _ONE_SECOND)
    elif _is_multiple(delta, _ONE_MILLI):
        return _maybe_add_count('L', delta / _ONE_MILLI)
    elif _is_multiple(delta, _ONE_MICRO):
        return _maybe_add_count('U', delta / _ONE_MICRO)
    else:
        return _maybe_add_count('N', delta)