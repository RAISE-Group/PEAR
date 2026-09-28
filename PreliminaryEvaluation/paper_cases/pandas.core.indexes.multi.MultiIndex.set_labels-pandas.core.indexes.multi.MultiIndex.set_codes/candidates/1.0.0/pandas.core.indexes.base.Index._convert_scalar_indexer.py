@Appender(_index_shared_docs['_convert_scalar_indexer'])
def _convert_scalar_indexer(self, key, kind=None):
    assert kind in ['ix', 'loc', 'getitem', 'iloc', None]
    if kind == 'iloc':
        return self._validate_indexer('positional', key, kind)
    if len(self) and (not isinstance(self, ABCMultiIndex)):
        if kind in ['getitem', 'ix'] and is_float(key):
            if not self.is_floating():
                return self._invalid_indexer('label', key)
        elif kind in ['loc'] and is_float(key):
            if self.inferred_type not in ['floating', 'mixed-integer-float', 'integer-na', 'string', 'unicode', 'mixed']:
                self._invalid_indexer('label', key)
        elif kind in ['loc'] and is_integer(key):
            if not self.holds_integer():
                self._invalid_indexer('label', key)
    return key