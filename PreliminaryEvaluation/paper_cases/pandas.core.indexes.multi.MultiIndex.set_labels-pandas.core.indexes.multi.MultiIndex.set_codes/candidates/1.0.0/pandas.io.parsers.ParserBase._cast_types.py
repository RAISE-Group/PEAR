def _cast_types(self, values, cast_type, column):
    """
        Cast values to specified type

        Parameters
        ----------
        values : ndarray
        cast_type : string or np.dtype
           dtype to cast values to
        column : string
            column name - used only for error reporting

        Returns
        -------
        converted : ndarray
        """
    if is_categorical_dtype(cast_type):
        known_cats = isinstance(cast_type, CategoricalDtype) and cast_type.categories is not None
        if not is_object_dtype(values) and (not known_cats):
            values = astype_nansafe(values, str)
        cats = Index(values).unique().dropna()
        values = Categorical._from_inferred_categories(cats, cats.get_indexer(values), cast_type, true_values=self.true_values)
    elif is_extension_array_dtype(cast_type):
        cast_type = pandas_dtype(cast_type)
        array_type = cast_type.construct_array_type()
        try:
            return array_type._from_sequence_of_strings(values, dtype=cast_type)
        except NotImplementedError:
            raise NotImplementedError(f'Extension Array: {array_type} must implement _from_sequence_of_strings in order to be used in parser methods')
    else:
        try:
            values = astype_nansafe(values, cast_type, copy=True, skipna=True)
        except ValueError:
            raise ValueError(f'Unable to convert column {column} to type {cast_type}')
    return values