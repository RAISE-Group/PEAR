def _do_date_conversions(self, names, data):
    if self.parse_dates is not None:
        data, names = _process_date_conversion(data, self._date_conv, self.parse_dates, self.index_col, self.index_names, names, keep_date_col=self.keep_date_col)
    return (names, data)