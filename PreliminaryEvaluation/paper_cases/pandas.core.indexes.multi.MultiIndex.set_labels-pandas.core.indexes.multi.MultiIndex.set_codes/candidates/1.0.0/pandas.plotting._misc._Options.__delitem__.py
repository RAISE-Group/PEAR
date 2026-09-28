def __delitem__(self, key):
    key = self._get_canonical_key(key)
    if key in self._DEFAULT_KEYS:
        raise ValueError(f'Cannot remove default parameter {key}')
    return super().__delitem__(key)