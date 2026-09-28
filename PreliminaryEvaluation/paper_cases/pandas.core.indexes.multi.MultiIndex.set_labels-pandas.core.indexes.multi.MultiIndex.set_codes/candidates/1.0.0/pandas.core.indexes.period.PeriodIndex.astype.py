@Appender(_index_shared_docs['astype'])
def astype(self, dtype, copy=True, how='start'):
    dtype = pandas_dtype(dtype)
    if is_datetime64_any_dtype(dtype):
        tz = getattr(dtype, 'tz', None)
        return self.to_timestamp(how=how).tz_localize(tz)
    return super().astype(dtype, copy=copy)