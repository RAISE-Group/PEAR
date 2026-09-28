def astype(self, dtype, copy=True):
    if isinstance(dtype, DummyDtype):
        if copy:
            return type(self)(self.data)
        return self
    return np.array(self, dtype=dtype, copy=copy)