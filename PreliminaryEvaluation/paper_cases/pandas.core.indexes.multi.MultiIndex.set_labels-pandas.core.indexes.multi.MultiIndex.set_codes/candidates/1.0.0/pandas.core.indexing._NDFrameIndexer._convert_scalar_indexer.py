def _convert_scalar_indexer(self, key, axis: int):
    ax = self.obj._get_axis(min(axis, self.ndim - 1))
    return ax._convert_scalar_indexer(key, kind=self.name)