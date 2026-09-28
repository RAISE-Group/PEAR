def _prepare_categoricals(self, data):
    """Check for categorical columns, retain categorical information for
        Stata file and convert categorical data to int"""
    is_cat = [is_categorical_dtype(data[col]) for col in data]
    self._is_col_cat = is_cat
    self._value_labels = []
    if not any(is_cat):
        return data
    get_base_missing_value = StataMissingValue.get_base_missing_value
    data_formatted = []
    for col, col_is_cat in zip(data, is_cat):
        if col_is_cat:
            svl = StataValueLabel(data[col], encoding=self._encoding)
            self._value_labels.append(svl)
            dtype = data[col].cat.codes.dtype
            if dtype == np.int64:
                raise ValueError('It is not possible to export int64-based categorical data to Stata.')
            values = data[col].cat.codes.values.copy()
            if values.max() >= get_base_missing_value(dtype):
                if dtype == np.int8:
                    dtype = np.int16
                elif dtype == np.int16:
                    dtype = np.int32
                else:
                    dtype = np.float64
                values = np.array(values, dtype=dtype)
            values[values == -1] = get_base_missing_value(dtype)
            data_formatted.append((col, values))
        else:
            data_formatted.append((col, data[col]))
    return DataFrame.from_dict(dict(data_formatted))