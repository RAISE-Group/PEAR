def _get_canonical_key(self, key):
    return self._ALIASES.get(key, key)