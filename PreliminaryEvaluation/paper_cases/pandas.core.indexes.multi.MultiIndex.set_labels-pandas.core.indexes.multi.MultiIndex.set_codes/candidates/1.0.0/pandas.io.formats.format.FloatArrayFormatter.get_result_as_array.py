def get_result_as_array(self) -> np.ndarray:
    """
        Returns the float values converted into strings using
        the parameters given at initialisation, as a numpy array
        """
    if self.formatter is not None:
        return np.array([self.formatter(x) for x in self.values])
    if self.fixed_width:
        threshold = get_option('display.chop_threshold')
    else:
        threshold = None

    def format_values_with(float_format):
        formatter = self._value_formatter(float_format, threshold)
        if self.justify == 'left':
            na_rep = ' ' + self.na_rep
        else:
            na_rep = self.na_rep
        values = self.values
        is_complex = is_complex_dtype(values)
        mask = isna(values)
        if hasattr(values, 'to_dense'):
            values = values.to_dense()
        values = np.array(values, dtype='object')
        values[mask] = na_rep
        imask = (~mask).ravel()
        values.flat[imask] = np.array([formatter(val) for val in values.ravel()[imask]])
        if self.fixed_width:
            if is_complex:
                result = _trim_zeros_complex(values, na_rep)
            else:
                result = _trim_zeros_float(values, na_rep)
            return np.asarray(result, dtype='object')
        return values
    float_format: Optional[float_format_type]
    if self.float_format is None:
        if self.fixed_width:
            float_format = partial('{value: .{digits:d}f}'.format, digits=self.digits)
        else:
            float_format = self.float_format
    else:
        float_format = lambda value: self.float_format % value
    formatted_values = format_values_with(float_format)
    if not self.fixed_width:
        return formatted_values
    if len(formatted_values) > 0:
        maxlen = max((len(x) for x in formatted_values))
        too_long = maxlen > self.digits + 6
    else:
        too_long = False
    with np.errstate(invalid='ignore'):
        abs_vals = np.abs(self.values)
        has_large_values = (abs_vals > 1000000.0).any()
        has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()
    if has_small_values or (too_long and has_large_values):
        float_format = partial('{value: .{digits:d}e}'.format, digits=self.digits)
        formatted_values = format_values_with(float_format)
    return formatted_values