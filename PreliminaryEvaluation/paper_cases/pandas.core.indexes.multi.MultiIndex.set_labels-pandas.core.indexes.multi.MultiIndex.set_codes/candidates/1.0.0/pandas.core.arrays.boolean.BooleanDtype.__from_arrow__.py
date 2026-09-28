def __from_arrow__(self, array):
    """Construct BooleanArray from passed pyarrow Array/ChunkedArray"""
    import pyarrow
    if isinstance(array, pyarrow.Array):
        chunks = [array]
    else:
        chunks = array.chunks
    results = []
    for arr in chunks:
        bool_arr = BooleanArray._from_sequence(np.array(arr))
        results.append(bool_arr)
    return BooleanArray._concat_same_type(results)