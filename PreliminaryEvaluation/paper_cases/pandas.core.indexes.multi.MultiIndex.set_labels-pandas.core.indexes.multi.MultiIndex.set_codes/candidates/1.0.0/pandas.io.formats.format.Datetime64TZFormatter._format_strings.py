def _format_strings(self) -> List[str]:
    """ we by definition have a TZ """
    values = self.values.astype(object)
    is_dates_only = _is_dates_only(values)
    formatter = self.formatter or _get_format_datetime64(is_dates_only, date_format=self.date_format)
    fmt_values = [formatter(x) for x in values]
    return fmt_values