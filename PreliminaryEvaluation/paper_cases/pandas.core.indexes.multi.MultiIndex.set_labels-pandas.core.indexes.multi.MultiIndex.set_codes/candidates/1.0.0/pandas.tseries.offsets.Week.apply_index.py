@apply_index_wraps
def apply_index(self, i):
    if self.weekday is None:
        asper = i.to_period('W')
        if not isinstance(asper._data, np.ndarray):
            asper = asper._data
        shifted = asper._time_shift(self.n)
        return shifted.to_timestamp() + i.to_perioddelta('W')
    else:
        return self._end_apply_index(i)