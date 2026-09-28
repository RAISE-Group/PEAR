def _maybe_parse_dates(self, values, index, try_parse_dates=True):
    if try_parse_dates and self._should_parse_dates(index):
        values = self._date_conv(values)
    return values