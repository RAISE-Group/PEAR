def __array__(self, dtype=None) -> np.ndarray:
    if dtype is None and self.tz:
        dtype = object
    return super().__array__(dtype=dtype)