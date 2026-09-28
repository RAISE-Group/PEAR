def __getitem__(self, item):
    if isinstance(item, numbers.Integral):
        return self.data[item]
    elif isinstance(item, slice) and item == slice(None):
        return type(self)(self.data)
    elif isinstance(item, slice):
        return type(self)(self.data[item])
    else:
        item = pd.api.indexers.check_array_indexer(self, item)
        if pd.api.types.is_bool_dtype(item.dtype):
            return self._from_sequence([x for x, m in zip(self, item) if m])
        return type(self)([self.data[i] for i in item])