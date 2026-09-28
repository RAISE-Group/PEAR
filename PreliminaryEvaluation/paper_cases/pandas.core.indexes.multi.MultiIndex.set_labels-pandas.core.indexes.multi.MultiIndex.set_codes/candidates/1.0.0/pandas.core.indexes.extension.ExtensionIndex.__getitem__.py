def __getitem__(self, key):
    result = self._data[key]
    if isinstance(result, type(self._data)):
        return type(self)(result, name=self.name)
    deprecate_ndim_indexing(result)
    return result