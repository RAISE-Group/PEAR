def _is_scalar_access(self, key: Tuple) -> bool:
    """
        Returns
        -------
        bool
        """
    if len(key) != self.ndim:
        return False
    for i, k in enumerate(key):
        if not is_integer(k):
            return False
        ax = self.obj.axes[i]
        if not ax.is_unique:
            return False
    return True