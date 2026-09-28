def _map_values(self, mapper, na_action=None):
    """
        An internal function that maps values using the input
        correspondence (which can be a dict, Series, or function).

        Parameters
        ----------
        mapper : function, dict, or Series
            The input correspondence object
        na_action : {None, 'ignore'}
            If 'ignore', propagate NA values, without passing them to the
            mapping function

        Returns
        -------
        Union[Index, MultiIndex], inferred
            The output of the mapping function applied to the index.
            If the function returns a tuple with more than one element
            a MultiIndex will be returned.

        """
    if is_dict_like(mapper):
        if isinstance(mapper, dict) and hasattr(mapper, '__missing__'):
            dict_with_default = mapper
            mapper = lambda x: dict_with_default[x]
        else:
            mapper = create_series_with_explicit_dtype(mapper, dtype_if_empty=np.float64)
    if isinstance(mapper, ABCSeries):
        if is_categorical_dtype(self._values):
            return self._values.map(mapper)
        if is_extension_array_dtype(self.dtype):
            values = self._values
        else:
            values = self.values
        indexer = mapper.index.get_indexer(values)
        new_values = algorithms.take_1d(mapper._values, indexer)
        return new_values
    if is_extension_array_dtype(self.dtype) and hasattr(self._values, 'map'):
        values = self._values
        if na_action is not None:
            raise NotImplementedError
        map_f = lambda values, f: values.map(f)
    else:
        values = self.astype(object)
        values = getattr(values, 'values', values)
        if na_action == 'ignore':

            def map_f(values, f):
                return lib.map_infer_mask(values, f, isna(values).view(np.uint8))
        else:
            map_f = lib.map_infer
    new_values = map_f(values, mapper)
    return new_values