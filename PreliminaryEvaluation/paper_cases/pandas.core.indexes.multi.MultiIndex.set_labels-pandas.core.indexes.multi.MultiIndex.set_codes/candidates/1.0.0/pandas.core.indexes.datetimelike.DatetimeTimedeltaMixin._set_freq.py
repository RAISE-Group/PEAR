def _set_freq(self, freq):
    """
        Set the _freq attribute on our underlying DatetimeArray.

        Parameters
        ----------
        freq : DateOffset, None, or "infer"
        """
    if freq is None:
        pass
    elif len(self) == 0 and isinstance(freq, DateOffset):
        pass
    else:
        assert freq == 'infer'
        freq = to_offset(self.inferred_freq)
    self._data._freq = freq