def __getitem__(self, item):
    if isinstance(item, numbers.Integral):
        return self._data[item]
    else:
        item = pd.api.indexers.check_array_indexer(self, item)
        return type(self)(self._data[item])