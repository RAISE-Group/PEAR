def _set_no_thousands_columns(self):
    noconvert_columns = set()

    def _set(x):
        if is_integer(x):
            noconvert_columns.add(x)
        else:
            noconvert_columns.add(self.columns.index(x))
    if isinstance(self.parse_dates, list):
        for val in self.parse_dates:
            if isinstance(val, list):
                for k in val:
                    _set(k)
            else:
                _set(val)
    elif isinstance(self.parse_dates, dict):
        for val in self.parse_dates.values():
            if isinstance(val, list):
                for k in val:
                    _set(k)
            else:
                _set(val)
    elif self.parse_dates:
        if isinstance(self.index_col, list):
            for k in self.index_col:
                _set(k)
        elif self.index_col is not None:
            _set(self.index_col)
    return noconvert_columns