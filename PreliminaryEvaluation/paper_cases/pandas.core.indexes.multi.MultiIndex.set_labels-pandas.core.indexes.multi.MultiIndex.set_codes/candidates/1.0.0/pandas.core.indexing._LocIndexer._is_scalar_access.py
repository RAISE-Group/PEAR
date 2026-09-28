def _is_scalar_access(self, key: Tuple) -> bool:
    """
        Returns
        -------
        bool
        """
    if len(key) != self.ndim:
        return False
    for i, k in enumerate(key):
        if not is_scalar(k):
            return False
        ax = self.obj.axes[i]
        if isinstance(ax, ABCMultiIndex):
            return False
        if isinstance(k, str) and ax._supports_partial_string_indexing:
            return False
        if not ax.is_unique:
            return False
    return True