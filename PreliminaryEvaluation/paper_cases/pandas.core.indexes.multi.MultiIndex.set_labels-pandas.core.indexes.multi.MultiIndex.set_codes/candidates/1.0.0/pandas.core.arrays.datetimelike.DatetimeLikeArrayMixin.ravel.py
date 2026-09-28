def ravel(self, *args, **kwargs):
    data = self._data.ravel(*args, **kwargs)
    return type(self)(data, dtype=self.dtype)