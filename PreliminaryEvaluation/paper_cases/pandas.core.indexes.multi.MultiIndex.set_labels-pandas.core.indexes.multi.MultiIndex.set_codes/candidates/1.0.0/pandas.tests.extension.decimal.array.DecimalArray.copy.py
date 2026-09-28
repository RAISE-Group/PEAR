def copy(self):
    return type(self)(self._data.copy())