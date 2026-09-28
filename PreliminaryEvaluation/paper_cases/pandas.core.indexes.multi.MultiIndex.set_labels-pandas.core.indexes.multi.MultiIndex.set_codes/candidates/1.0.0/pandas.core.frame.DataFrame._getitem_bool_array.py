def _getitem_bool_array(self, key):
    if isinstance(key, Series) and (not key.index.equals(self.index)):
        warnings.warn('Boolean Series key will be reindexed to match DataFrame index.', UserWarning, stacklevel=3)
    elif len(key) != len(self.index):
        raise ValueError(f'Item wrong length {len(key)} instead of {len(self.index)}.')
    key = check_bool_indexer(self.index, key)
    indexer = key.nonzero()[0]
    return self._take_with_is_copy(indexer, axis=0)