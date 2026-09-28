def _convert_for_op(self, value):
    """
        Convert value to be insertable to ndarray.
        """
    if is_bool(value) or is_bool_dtype(value):
        raise TypeError
    return value