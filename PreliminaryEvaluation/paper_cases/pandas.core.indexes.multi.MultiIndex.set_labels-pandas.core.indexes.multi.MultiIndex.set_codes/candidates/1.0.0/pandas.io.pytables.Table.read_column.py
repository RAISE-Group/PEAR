def read_column(self, column: str, where=None, start: Optional[int]=None, stop: Optional[int]=None):
    """return a single column from the table, generally only indexables
        are interesting
        """
    self.validate_version()
    if not self.infer_axes():
        return False
    if where is not None:
        raise TypeError('read_column does not currently accept a where clause')
    for a in self.axes:
        if column == a.name:
            if not a.is_data_indexable:
                raise ValueError(f'column [{column}] can not be extracted individually; it is not data indexable')
            c = getattr(self.table.cols, column)
            a.set_info(self.info)
            col_values = a.convert(c[start:stop], nan_rep=self.nan_rep, encoding=self.encoding, errors=self.errors)
            return Series(_set_tz(col_values[1], a.tz), name=column)
    raise KeyError(f'column [{column}] not found in the table')