def _get_values(self, indexer):
    try:
        return self._constructor(self._data.get_slice(indexer), fastpath=True).__finalize__(self)
    except ValueError:
        return self._values[indexer]