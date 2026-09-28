def check_keys_split(self, decoded):
    """
        Checks that dict has only the appropriate keys for orient='split'.
        """
    bad_keys = set(decoded.keys()).difference(set(self._split_keys))
    if bad_keys:
        bad_keys = ', '.join(bad_keys)
        raise ValueError(f'JSON data had unexpected key(s): {bad_keys}')