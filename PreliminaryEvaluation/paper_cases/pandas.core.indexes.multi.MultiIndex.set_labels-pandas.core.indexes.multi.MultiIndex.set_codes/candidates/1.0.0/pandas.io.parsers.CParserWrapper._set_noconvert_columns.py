def _set_noconvert_columns(self):
    """
        Set the columns that should not undergo dtype conversions.

        Currently, any column that is involved with date parsing will not
        undergo such conversions.
        """
    names = self.orig_names
    if self.usecols_dtype == 'integer':
        usecols = list(self.usecols)
        usecols.sort()
    elif callable(self.usecols) or self.usecols_dtype not in ('empty', None):
        usecols = self.names[:]
    else:
        usecols = None

    def _set(x):
        if usecols is not None and is_integer(x):
            x = usecols[x]
        if not is_integer(x):
            x = names.index(x)
        self._reader.set_noconvert(x)
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