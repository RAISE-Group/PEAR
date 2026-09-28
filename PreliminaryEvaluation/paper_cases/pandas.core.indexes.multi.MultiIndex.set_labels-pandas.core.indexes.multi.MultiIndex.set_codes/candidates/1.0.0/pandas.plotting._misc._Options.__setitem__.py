def __setitem__(self, key, value):
    key = self._get_canonical_key(key)
    return super().__setitem__(key, value)