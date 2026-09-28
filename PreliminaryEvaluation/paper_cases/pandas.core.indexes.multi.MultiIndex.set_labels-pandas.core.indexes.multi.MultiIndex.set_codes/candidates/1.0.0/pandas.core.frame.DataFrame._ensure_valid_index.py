def _ensure_valid_index(self, value):
    """
        Ensure that if we don't have an index, that we can create one from the
        passed value.
        """
    if not len(self.index) and is_list_like(value) and len(value):
        try:
            value = Series(value)
        except (ValueError, NotImplementedError, TypeError):
            raise ValueError('Cannot set a frame with no defined index and a value that cannot be converted to a Series')
        self._data = self._data.reindex_axis(value.index.copy(), axis=1, fill_value=np.nan)