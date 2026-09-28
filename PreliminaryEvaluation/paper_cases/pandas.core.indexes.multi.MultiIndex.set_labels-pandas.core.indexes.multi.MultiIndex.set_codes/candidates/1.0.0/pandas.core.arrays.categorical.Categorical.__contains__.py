def __contains__(self, key) -> bool:
    """
        Returns True if `key` is in this Categorical.
        """
    if is_scalar(key) and isna(key):
        return self.isna().any()
    return contains(self, key, container=self._codes)