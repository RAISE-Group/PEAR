@Appender(_index_shared_docs['astype'])
def astype(self, dtype, copy=True):
    dtype = pandas_dtype(dtype)
    if is_timedelta64_dtype(dtype) and (not is_timedelta64_ns_dtype(dtype)):
        result = self._data.astype(dtype, copy=copy)
        if self.hasnans:
            return Index(result, name=self.name)
        return Index(result.astype('i8'), name=self.name)
    return DatetimeIndexOpsMixin.astype(self, dtype, copy=copy)