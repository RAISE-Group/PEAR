def _sqlalchemy_type(self, col):
    dtype = self.dtype or {}
    if col.name in dtype:
        return self.dtype[col.name]
    col_type = lib.infer_dtype(col, skipna=True)
    from sqlalchemy.types import BigInteger, Integer, Float, Text, Boolean, DateTime, Date, Time, TIMESTAMP
    if col_type == 'datetime64' or col_type == 'datetime':
        try:
            if col.dt.tz is not None:
                return TIMESTAMP(timezone=True)
        except AttributeError:
            if col.tz is not None:
                return TIMESTAMP(timezone=True)
        return DateTime
    if col_type == 'timedelta64':
        warnings.warn("the 'timedelta' type is not supported, and will be written as integer values (ns frequency) to the database.", UserWarning, stacklevel=8)
        return BigInteger
    elif col_type == 'floating':
        if col.dtype == 'float32':
            return Float(precision=23)
        else:
            return Float(precision=53)
    elif col_type == 'integer':
        if col.dtype == 'int32':
            return Integer
        else:
            return BigInteger
    elif col_type == 'boolean':
        return Boolean
    elif col_type == 'date':
        return Date
    elif col_type == 'time':
        return Time
    elif col_type == 'complex':
        raise ValueError('Complex datatypes not supported')
    return Text