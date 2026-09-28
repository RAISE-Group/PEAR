def __array__(self, dtype=None) -> np.ndarray:
    if is_object_dtype(dtype):
        return np.array(list(self), dtype=object)
    return self._data