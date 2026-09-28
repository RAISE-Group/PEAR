def _convert_to_ndarrays(self, dct, na_values, na_fvalues, verbose=False, converters=None, dtypes=None):
    result = {}
    for c, values in dct.items():
        conv_f = None if converters is None else converters.get(c, None)
        if isinstance(dtypes, dict):
            cast_type = dtypes.get(c, None)
        else:
            cast_type = dtypes
        if self.na_filter:
            col_na_values, col_na_fvalues = _get_na_values(c, na_values, na_fvalues, self.keep_default_na)
        else:
            col_na_values, col_na_fvalues = (set(), set())
        if conv_f is not None:
            if cast_type is not None:
                warnings.warn(f'Both a converter and dtype were specified for column {c} - only the converter will be used', ParserWarning, stacklevel=7)
            try:
                values = lib.map_infer(values, conv_f)
            except ValueError:
                mask = algorithms.isin(values, list(na_values)).view(np.uint8)
                values = lib.map_infer_mask(values, conv_f, mask)
            cvals, na_count = self._infer_types(values, set(col_na_values) | col_na_fvalues, try_num_bool=False)
        else:
            is_str_or_ea_dtype = is_string_dtype(cast_type) or is_extension_array_dtype(cast_type)
            try_num_bool = not (cast_type and is_str_or_ea_dtype)
            cvals, na_count = self._infer_types(values, set(col_na_values) | col_na_fvalues, try_num_bool)
            if cast_type and (not is_dtype_equal(cvals, cast_type) or is_extension_array_dtype(cast_type)):
                try:
                    if is_bool_dtype(cast_type) and (not is_categorical_dtype(cast_type)) and (na_count > 0):
                        raise ValueError(f'Bool column has NA values in column {c}')
                except (AttributeError, TypeError):
                    pass
                cvals = self._cast_types(cvals, cast_type, c)
        result[c] = cvals
        if verbose and na_count:
            print(f'Filled {na_count} NA values in column {c!s}')
    return result