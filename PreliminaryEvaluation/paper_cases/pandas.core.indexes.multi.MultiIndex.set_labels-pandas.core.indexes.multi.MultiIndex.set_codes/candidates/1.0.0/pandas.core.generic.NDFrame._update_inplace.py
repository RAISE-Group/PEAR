def _update_inplace(self, result, verify_is_copy: bool_t=True) -> None:
    """
        Replace self internals with result.

        Parameters
        ----------
        verify_is_copy : bool, default True
            Provide is_copy checks.
        """
    self._reset_cache()
    self._clear_item_cache()
    self._data = getattr(result, '_data', result)
    self._maybe_update_cacher(verify_is_copy=verify_is_copy)