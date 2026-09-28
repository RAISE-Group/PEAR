def astype(self, dtype, copy=True):
    if isinstance(dtype, type(self.dtype)) and dtype == self.dtype:
        if copy:
            return self.copy()
        return self
    return super().astype(dtype, copy)