@Appender(_NDFrameIndexer._validate_key.__doc__)
def _validate_key(self, key, axis: int):
    if isinstance(key, slice):
        return
    if com.is_bool_indexer(key):
        return
    if not is_list_like_indexer(key):
        self._convert_scalar_indexer(key, axis)