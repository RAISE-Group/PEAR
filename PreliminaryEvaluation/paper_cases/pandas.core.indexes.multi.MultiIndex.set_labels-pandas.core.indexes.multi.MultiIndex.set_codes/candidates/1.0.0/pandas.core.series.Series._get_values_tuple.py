def _get_values_tuple(self, key):
    if com.any_none(*key):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', 'Support for multi-dim', DeprecationWarning)
            return self._get_values(key)
    if not isinstance(self.index, MultiIndex):
        raise ValueError('Can only tuple-index with a MultiIndex')
    indexer, new_index = self.index.get_loc_level(key)
    return self._constructor(self._values[indexer], index=new_index).__finalize__(self)