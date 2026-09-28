def __from_arrow__(self, array):
    """Construct StringArray from passed pyarrow Array/ChunkedArray"""
    import pyarrow
    if isinstance(array, pyarrow.Array):
        chunks = [array]
    else:
        chunks = array.chunks
    results = []
    for arr in chunks:
        str_arr = StringArray._from_sequence(np.array(arr))
        results.append(str_arr)
    return StringArray._concat_same_type(results)