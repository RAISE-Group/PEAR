def _format_strings(self) -> List[str]:
    values = self.values
    if isinstance(values, (ABCIndexClass, ABCSeries)):
        values = values._values
    formatter = values._formatter(boxed=True)
    if is_categorical_dtype(values.dtype):
        array = values._internal_get_values()
    else:
        array = np.asarray(values)
    fmt_values = format_array(array, formatter, float_format=self.float_format, na_rep=self.na_rep, digits=self.digits, space=self.space, justify=self.justify, leading_space=self.leading_space)
    return fmt_values