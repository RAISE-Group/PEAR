def isna(self):
    return np.array([x.is_nan() for x in self._data], dtype=bool)