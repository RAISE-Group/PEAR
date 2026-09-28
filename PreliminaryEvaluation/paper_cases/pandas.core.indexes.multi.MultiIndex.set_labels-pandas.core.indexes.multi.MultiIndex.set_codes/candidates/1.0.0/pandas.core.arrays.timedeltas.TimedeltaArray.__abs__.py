def __abs__(self):
    return type(self)(np.abs(self._data))