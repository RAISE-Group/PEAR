@Appender(_index_shared_docs['_maybe_cast_slice_bound'])
def _maybe_cast_slice_bound(self, label, side, kind):
    assert kind in ['ix', 'loc', 'getitem', None]
    if is_float(label):
        if not (kind in ['ix'] and (self.holds_integer() or self.is_floating())):
            self._invalid_indexer('slice', label)
    elif is_integer(label):
        self._invalid_indexer('slice', label)
    return label