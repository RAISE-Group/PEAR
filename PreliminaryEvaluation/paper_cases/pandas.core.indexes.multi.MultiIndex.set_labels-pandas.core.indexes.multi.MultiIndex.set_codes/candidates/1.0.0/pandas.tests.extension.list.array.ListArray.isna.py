def isna(self):
    return np.array([not isinstance(x, list) and np.isnan(x) for x in self.data], dtype=bool)