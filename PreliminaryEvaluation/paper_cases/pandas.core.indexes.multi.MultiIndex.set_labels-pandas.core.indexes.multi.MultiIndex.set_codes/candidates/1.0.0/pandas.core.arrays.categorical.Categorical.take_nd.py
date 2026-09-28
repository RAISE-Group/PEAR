def take_nd(self, indexer, allow_fill: bool=False, fill_value=None):
    warn('Categorical.take_nd is deprecated, use Categorical.take instead', FutureWarning, stacklevel=2)
    return self.take(indexer, allow_fill=allow_fill, fill_value=fill_value)