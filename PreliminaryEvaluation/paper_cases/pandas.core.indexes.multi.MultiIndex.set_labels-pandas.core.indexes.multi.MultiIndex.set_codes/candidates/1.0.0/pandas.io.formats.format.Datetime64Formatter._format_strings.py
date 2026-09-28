def _format_strings(self) -> List[str]:
    """ we by definition have DO NOT have a TZ """
    values = self.values
    if not isinstance(values, DatetimeIndex):
        values = DatetimeIndex(values)
    if self.formatter is not None and callable(self.formatter):
        return [self.formatter(x) for x in values]
    fmt_values = format_array_from_datetime(values.asi8.ravel(), format=_get_format_datetime64_from_values(values, self.date_format), na_rep=self.nat_rep).reshape(values.shape)
    return fmt_values.tolist()