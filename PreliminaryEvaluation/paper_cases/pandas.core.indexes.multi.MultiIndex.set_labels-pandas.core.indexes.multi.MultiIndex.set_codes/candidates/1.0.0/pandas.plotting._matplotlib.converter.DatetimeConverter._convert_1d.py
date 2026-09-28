@staticmethod
def _convert_1d(values, unit, axis):

    def try_parse(values):
        try:
            return _dt_to_float_ordinal(tools.to_datetime(values))
        except Exception:
            return values
    if isinstance(values, (datetime, pydt.date)):
        return _dt_to_float_ordinal(values)
    elif isinstance(values, np.datetime64):
        return _dt_to_float_ordinal(tslibs.Timestamp(values))
    elif isinstance(values, pydt.time):
        return dates.date2num(values)
    elif is_integer(values) or is_float(values):
        return values
    elif isinstance(values, str):
        return try_parse(values)
    elif isinstance(values, (list, tuple, np.ndarray, Index, ABCSeries)):
        if isinstance(values, ABCSeries):
            values = Index(values)
        if isinstance(values, Index):
            values = values.values
        if not isinstance(values, np.ndarray):
            values = com.asarray_tuplesafe(values)
        if is_integer_dtype(values) or is_float_dtype(values):
            return values
        try:
            values = tools.to_datetime(values)
            if isinstance(values, Index):
                values = _dt_to_float_ordinal(values)
            else:
                values = [_dt_to_float_ordinal(x) for x in values]
        except Exception:
            values = _dt_to_float_ordinal(values)
    return values