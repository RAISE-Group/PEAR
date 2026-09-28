def astype(self, dtype, copy=True):
    if isinstance(dtype, type(self.dtype)) and dtype == self.dtype:
        if copy:
            return self.copy()
        return self
    return np.array([dict(x) for x in self], dtype=dtype, copy=copy)