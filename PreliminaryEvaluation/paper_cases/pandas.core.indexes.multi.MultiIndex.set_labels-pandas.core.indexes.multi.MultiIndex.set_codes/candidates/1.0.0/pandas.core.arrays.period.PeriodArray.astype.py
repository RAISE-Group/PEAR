def astype(self, dtype, copy=True):
    dtype = pandas_dtype(dtype)
    if is_period_dtype(dtype):
        return self.asfreq(dtype.freq)
    return super().astype(dtype, copy=copy)