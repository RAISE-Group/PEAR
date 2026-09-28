@unpack_zerodim_and_defer('__add__')
def __add__(self, other):
    if other is NaT:
        result = self._add_nat()
    elif isinstance(other, (Tick, timedelta, np.timedelta64)):
        result = self._add_delta(other)
    elif isinstance(other, DateOffset):
        result = self._add_offset(other)
    elif isinstance(other, (datetime, np.datetime64)):
        result = self._add_datetimelike_scalar(other)
    elif lib.is_integer(other):
        if not is_period_dtype(self):
            raise integer_op_not_supported(self)
        result = self._time_shift(other)
    elif is_timedelta64_dtype(other):
        result = self._add_delta(other)
    elif is_object_dtype(other):
        result = self._addsub_object_array(other, operator.add)
    elif is_datetime64_dtype(other) or is_datetime64tz_dtype(other):
        return self._add_datetime_arraylike(other)
    elif is_integer_dtype(other):
        if not is_period_dtype(self):
            raise integer_op_not_supported(self)
        result = self._addsub_int_array(other, operator.add)
    else:
        return NotImplemented
    if is_timedelta64_dtype(result) and isinstance(result, np.ndarray):
        from pandas.core.arrays import TimedeltaArray
        return TimedeltaArray(result)
    return result