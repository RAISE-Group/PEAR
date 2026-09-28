def astype(self, dtype, copy=True):
    dtype = pandas_dtype(dtype)
    if is_datetime64_ns_dtype(dtype) and (not is_dtype_equal(dtype, self.dtype)):
        new_tz = getattr(dtype, 'tz', None)
        if getattr(self.dtype, 'tz', None) is None:
            return self.tz_localize(new_tz)
        result = self.tz_convert(new_tz)
        if new_tz is None:
            result = result._data
        return result
    elif is_datetime64tz_dtype(self.dtype) and is_dtype_equal(self.dtype, dtype):
        if copy:
            return self.copy()
        return self
    elif is_period_dtype(dtype):
        return self.to_period(freq=dtype.freq)
    return dtl.DatetimeLikeArrayMixin.astype(self, dtype, copy)