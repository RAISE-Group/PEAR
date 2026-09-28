def copy(self):
    return type(self)(copy.copy(self._data))