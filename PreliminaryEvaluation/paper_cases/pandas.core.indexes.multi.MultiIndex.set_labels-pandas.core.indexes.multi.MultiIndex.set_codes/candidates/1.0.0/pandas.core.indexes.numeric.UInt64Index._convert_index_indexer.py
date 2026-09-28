@Appender(_index_shared_docs['_convert_index_indexer'])
def _convert_index_indexer(self, keyarr):
    if keyarr.is_integer():
        return keyarr.astype(np.uint64)
    return keyarr