@staticmethod
def _convert_1d(values, units, axis):
    if not hasattr(axis, 'freq'):
        raise TypeError('Axis must have `freq` set to convert to Periods')
    valid_types = (str, datetime, Period, pydt.date, pydt.time, np.datetime64)
    if isinstance(values, valid_types) or is_integer(values) or is_float(values):
        return get_datevalue(values, axis.freq)
    elif isinstance(values, PeriodIndex):
        return values.asfreq(axis.freq)._ndarray_values
    elif isinstance(values, Index):
        return values.map(lambda x: get_datevalue(x, axis.freq))
    elif lib.infer_dtype(values, skipna=False) == 'period':
        return PeriodIndex(values, freq=axis.freq)._ndarray_values
    elif isinstance(values, (list, tuple, np.ndarray, Index)):
        return [get_datevalue(x, axis.freq) for x in values]
    return values