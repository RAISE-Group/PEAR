def __getitem__(self, key):
    from pandas.core.indexing import check_bool_indexer
    if isinstance(key, tuple):
        if len(key) > 1:
            raise IndexError('too many indices for array.')
        key = key[0]
    if is_integer(key):
        return self._get_val_at(key)
    elif isinstance(key, tuple):
        data_slice = self.to_dense()[key]
    elif isinstance(key, slice):
        if key == slice(None):
            return self.copy()
        indices = np.arange(len(self), dtype=np.int32)[key]
        return self.take(indices)
    else:
        if isinstance(key, SparseArray):
            if is_bool_dtype(key):
                key = key.to_dense()
            else:
                key = np.asarray(key)
        key = check_array_indexer(self, key)
        if com.is_bool_indexer(key):
            key = check_bool_indexer(self, key)
            return self.take(np.arange(len(key), dtype=np.int32)[key])
        elif hasattr(key, '__len__'):
            return self.take(key)
        else:
            raise ValueError(f"Cannot slice with '{key}'")
    return type(self)(data_slice, kind=self.kind)