@Appender(_index_shared_docs['_convert_arr_indexer'])
def _convert_arr_indexer(self, keyarr):
    dtype = None
    if is_integer_dtype(keyarr) or lib.infer_dtype(keyarr, skipna=False) == 'integer':
        dtype = np.uint64
    return com.asarray_tuplesafe(keyarr, dtype=dtype)