def _get_dtype(self, sqltype):
    from sqlalchemy.types import Integer, Float, Boolean, DateTime, Date, TIMESTAMP
    if isinstance(sqltype, Float):
        return float
    elif isinstance(sqltype, Integer):
        return np.dtype('int64')
    elif isinstance(sqltype, TIMESTAMP):
        if not sqltype.timezone:
            return datetime
        return DatetimeTZDtype
    elif isinstance(sqltype, DateTime):
        return datetime
    elif isinstance(sqltype, Date):
        return date
    elif isinstance(sqltype, Boolean):
        return bool
    return object