def effective_dtype(self, dtype):
    if dtype is None:
        return np.uint8
    return dtype