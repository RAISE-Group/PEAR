def get_values(self, dtype=None):
    """
        Returns an ndarray of values.

        Parameters
        ----------
        dtype : np.dtype
            Only `object`-like dtypes are respected here (not sure
            why).

        Returns
        -------
        values : ndarray
            When ``dtype=object``, then and object-dtype ndarray of
            boxed values is returned. Otherwise, an M8[ns] ndarray
            is returned.

            DatetimeArray is always 1-d. ``get_values`` will reshape
            the return value to be the same dimensionality as the
            block.
        """
    values = self.values
    if is_object_dtype(dtype):
        values = values.astype(object)
    values = np.asarray(values)
    if self.ndim == 2:
        values = values.reshape(1, -1)
    return values