def _infer_types(self, values, na_values, try_num_bool=True):
    """
        Infer types of values, possibly casting

        Parameters
        ----------
        values : ndarray
        na_values : set
        try_num_bool : bool, default try
           try to cast values to numeric (first preference) or boolean

        Returns
        -------
        converted : ndarray
        na_count : int
        """
    na_count = 0
    if issubclass(values.dtype.type, (np.number, np.bool_)):
        mask = algorithms.isin(values, list(na_values))
        na_count = mask.sum()
        if na_count > 0:
            if is_integer_dtype(values):
                values = values.astype(np.float64)
            np.putmask(values, mask, np.nan)
        return (values, na_count)
    if try_num_bool and is_object_dtype(values.dtype):
        try:
            result = lib.maybe_convert_numeric(values, na_values, False)
        except (ValueError, TypeError):
            result = values
            na_count = parsers.sanitize_objects(result, na_values, False)
        else:
            na_count = isna(result).sum()
    else:
        result = values
        if values.dtype == np.object_:
            na_count = parsers.sanitize_objects(values, na_values, False)
    if result.dtype == np.object_ and try_num_bool:
        result = libops.maybe_convert_bool(np.asarray(values), true_values=self.true_values, false_values=self.false_values)
    return (result, na_count)