@cache_readonly
def _isnan(self):
    """
        Return if each value is NaN.
        """
    if self._can_hold_na:
        return isna(self)
    else:
        values = np.empty(len(self), dtype=np.bool_)
        values.fill(False)
        return values