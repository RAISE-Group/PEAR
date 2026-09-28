def __array__(self, dtype=None) -> np.ndarray:
    return np.array(list(self), dtype=object)