def __isub__(self, other):
    result = self - other
    self[:] = result[:]
    if not is_period_dtype(self):
        self._freq = result._freq
    return self