def astype(self, dtype, copy=True):
    if isinstance(dtype, type(self.dtype)):
        return type(self)(self._data, context=dtype.context)
    return np.asarray(self, dtype=dtype)