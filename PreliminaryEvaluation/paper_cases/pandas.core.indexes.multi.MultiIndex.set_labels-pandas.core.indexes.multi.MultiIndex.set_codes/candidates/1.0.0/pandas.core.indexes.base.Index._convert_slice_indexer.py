@Appender(_index_shared_docs['_convert_slice_indexer'])
def _convert_slice_indexer(self, key: slice, kind=None):
    assert kind in ['ix', 'loc', 'getitem', 'iloc', None]
    if kind == 'iloc':
        return slice(self._validate_indexer('slice', key.start, kind), self._validate_indexer('slice', key.stop, kind), self._validate_indexer('slice', key.step, kind))
    start, stop, step = (key.start, key.stop, key.step)

    def is_int(v):
        return v is None or is_integer(v)
    is_null_slicer = start is None and stop is None
    is_index_slice = is_int(start) and is_int(stop)
    is_positional = is_index_slice and (not (self.is_integer() or self.is_categorical()))
    if kind == 'getitem':
        '\n            called from the getitem slicers, validate that we are in fact\n            integers\n            '
        if self.is_integer() or is_index_slice:
            return slice(self._validate_indexer('slice', key.start, kind), self._validate_indexer('slice', key.stop, kind), self._validate_indexer('slice', key.step, kind))
    try:
        if is_positional and self.is_mixed():
            if start is not None:
                self.get_loc(start)
            if stop is not None:
                self.get_loc(stop)
            is_positional = False
    except KeyError:
        if self.inferred_type in ['mixed-integer-float', 'integer-na']:
            raise
    if is_null_slicer:
        indexer = key
    elif is_positional:
        indexer = key
    else:
        indexer = self.slice_indexer(start, stop, step, kind=kind)
    return indexer