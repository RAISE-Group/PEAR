def __getitem__(self, key):
    key = lib.item_from_zerodim(key)
    key = com.apply_if_callable(key, self)
    if is_hashable(key):
        if self.columns.is_unique and key in self.columns:
            if self.columns.nlevels > 1:
                return self._getitem_multilevel(key)
            return self._get_item_cache(key)
    indexer = convert_to_index_sliceable(self, key)
    if indexer is not None:
        return self._slice(indexer, axis=0)
    if isinstance(key, DataFrame):
        return self.where(key)
    if com.is_bool_indexer(key):
        return self._getitem_bool_array(key)
    is_single_key = isinstance(key, tuple) or not is_list_like(key)
    if is_single_key:
        if self.columns.nlevels > 1:
            return self._getitem_multilevel(key)
        indexer = self.columns.get_loc(key)
        if is_integer(indexer):
            indexer = [indexer]
    else:
        if is_iterator(key):
            key = list(key)
        indexer = self.loc._get_listlike_indexer(key, axis=1, raise_missing=True)[1]
    if getattr(indexer, 'dtype', None) == bool:
        indexer = np.where(indexer)[0]
    data = self._take_with_is_copy(indexer, axis=1)
    if is_single_key:
        if data.shape[1] == 1 and (not isinstance(self.columns, ABCMultiIndex)):
            data = data[key]
    return data