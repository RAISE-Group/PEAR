@Appender(_index_shared_docs['_maybe_cast_slice_bound'])
def _maybe_cast_slice_bound(self, label, side, kind):
    assert kind in ['ix', 'loc', 'getitem', None]
    return self._maybe_cast_indexer(label)