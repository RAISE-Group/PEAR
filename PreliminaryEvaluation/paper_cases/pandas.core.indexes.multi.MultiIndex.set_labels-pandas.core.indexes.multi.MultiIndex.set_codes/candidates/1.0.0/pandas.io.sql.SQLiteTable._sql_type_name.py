def _sql_type_name(self, col):
    dtype = self.dtype or {}
    if col.name in dtype:
        return dtype[col.name]
    col_type = lib.infer_dtype(col, skipna=True)
    if col_type == 'timedelta64':
        warnings.warn("the 'timedelta' type is not supported, and will be written as integer values (ns frequency) to the database.", UserWarning, stacklevel=8)
        col_type = 'integer'
    elif col_type == 'datetime64':
        col_type = 'datetime'
    elif col_type == 'empty':
        col_type = 'string'
    elif col_type == 'complex':
        raise ValueError('Complex datatypes not supported')
    if col_type not in _SQL_TYPES:
        col_type = 'string'
    return _SQL_TYPES[col_type]