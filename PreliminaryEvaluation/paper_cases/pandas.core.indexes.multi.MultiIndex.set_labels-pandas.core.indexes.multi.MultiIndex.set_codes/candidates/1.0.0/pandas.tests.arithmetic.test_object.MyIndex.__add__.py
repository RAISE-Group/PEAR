def __add__(self, other):
    self._calls += 1
    return self._simple_new(self._index_data)