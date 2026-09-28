def _coerce_scalar_to_index(self, item):
    """
        We need to coerce a scalar to a compat for our index type.

        Parameters
        ----------
        item : scalar item to coerce
        """
    dtype = self.dtype
    if self._is_numeric_dtype and isna(item):
        dtype = None
    return Index([item], dtype=dtype, **self._get_attributes_dict())