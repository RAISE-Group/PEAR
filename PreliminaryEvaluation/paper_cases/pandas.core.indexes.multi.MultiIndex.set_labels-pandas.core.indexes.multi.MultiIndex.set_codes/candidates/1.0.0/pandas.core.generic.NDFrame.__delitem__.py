def __delitem__(self, key) -> None:
    """
        Delete item
        """
    deleted = False
    maybe_shortcut = False
    if self.ndim == 2 and isinstance(self.columns, MultiIndex):
        try:
            maybe_shortcut = key not in self.columns._engine
        except TypeError:
            pass
    if maybe_shortcut:
        if not isinstance(key, tuple):
            key = (key,)
        for col in self.columns:
            if isinstance(col, tuple) and col[:len(key)] == key:
                del self[col]
                deleted = True
    if not deleted:
        self._data.delete(key)
    try:
        del self._item_cache[key]
    except KeyError:
        pass