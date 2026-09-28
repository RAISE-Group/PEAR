def __contains__(self, key) -> bool:
    key = self._get_canonical_key(key)
    return super().__contains__(key)