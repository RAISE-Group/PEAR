def __getitem__(self, key):
    key = self._get_canonical_key(key)
    if key not in self:
        raise ValueError(f'{key} is not a valid pandas plotting option')
    return super().__getitem__(key)