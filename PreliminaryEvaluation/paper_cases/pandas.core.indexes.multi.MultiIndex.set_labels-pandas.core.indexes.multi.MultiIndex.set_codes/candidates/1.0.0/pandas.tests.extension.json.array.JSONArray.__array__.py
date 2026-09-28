def __array__(self, dtype=None):
    if dtype is None:
        dtype = object
    return np.asarray(self.data, dtype=dtype)