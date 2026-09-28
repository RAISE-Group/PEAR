def astype(self, dtype, copy=True):
    dtype = pandas_dtype(dtype)
    if is_timedelta64_dtype(dtype) and (not is_timedelta64_ns_dtype(dtype)):
        if self._hasnans:
            result = self._data.astype(dtype, copy=False)
            values = self._maybe_mask_results(result, fill_value=None, convert='float64')
            return values
        result = self._data.astype(dtype, copy=copy)
        return result.astype('i8')
    elif is_timedelta64_ns_dtype(dtype):
        if copy:
            return self.copy()
        return self
    return dtl.DatetimeLikeArrayMixin.astype(self, dtype, copy=copy)