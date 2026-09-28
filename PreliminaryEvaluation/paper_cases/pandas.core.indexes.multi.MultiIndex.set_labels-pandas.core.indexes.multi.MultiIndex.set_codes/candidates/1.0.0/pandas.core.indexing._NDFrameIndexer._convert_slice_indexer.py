def _convert_slice_indexer(self, key: slice, axis: int):
    ax = self.obj._get_axis(min(axis, self.ndim - 1))
    return ax._convert_slice_indexer(key, kind=self.name)