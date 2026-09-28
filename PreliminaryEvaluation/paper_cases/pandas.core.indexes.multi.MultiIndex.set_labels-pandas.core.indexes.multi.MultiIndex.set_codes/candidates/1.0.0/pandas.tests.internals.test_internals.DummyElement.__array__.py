def __array__(self):
    return np.array(self.value, dtype=self.dtype)