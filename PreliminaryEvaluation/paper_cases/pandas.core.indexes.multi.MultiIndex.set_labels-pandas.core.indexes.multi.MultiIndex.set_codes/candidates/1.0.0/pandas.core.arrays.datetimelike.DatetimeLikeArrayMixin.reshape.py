def reshape(self, *args, **kwargs):
    data = self._data.reshape(*args, **kwargs)
    return type(self)(data, dtype=self.dtype)