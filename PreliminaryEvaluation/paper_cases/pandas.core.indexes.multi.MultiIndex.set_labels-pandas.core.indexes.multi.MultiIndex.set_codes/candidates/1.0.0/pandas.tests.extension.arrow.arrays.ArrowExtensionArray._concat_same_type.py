@classmethod
def _concat_same_type(cls, to_concat):
    chunks = list(itertools.chain.from_iterable((x._data.chunks for x in to_concat)))
    arr = pa.chunked_array(chunks)
    return cls(arr)