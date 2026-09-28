def isna(self):
    return np.array([x == self.dtype.na_value for x in self.data], dtype=bool)