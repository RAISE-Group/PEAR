def _try_convert_dates(self):
    if self.obj is None:
        return
    convert_dates = self.convert_dates
    if convert_dates is True:
        convert_dates = []
    convert_dates = set(convert_dates)

    def is_ok(col) -> bool:
        """
            Return if this col is ok to try for a date parse.
            """
        if not isinstance(col, str):
            return False
        col_lower = col.lower()
        if col_lower.endswith('_at') or col_lower.endswith('_time') or col_lower == 'modified' or (col_lower == 'date') or (col_lower == 'datetime') or col_lower.startswith('timestamp'):
            return True
        return False
    self._process_converter(lambda col, c: self._try_convert_to_date(c), lambda col, c: self.keep_default_dates and is_ok(col) or col in convert_dates)