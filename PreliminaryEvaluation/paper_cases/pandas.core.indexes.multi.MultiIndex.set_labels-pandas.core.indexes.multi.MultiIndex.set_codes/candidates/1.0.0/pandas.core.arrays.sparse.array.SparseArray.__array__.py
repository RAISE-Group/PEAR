def __array__(self, dtype=None, copy=True) -> np.ndarray:
    fill_value = self.fill_value
    if self.sp_index.ngaps == 0:
        return self.sp_values
    if dtype is None:
        if is_datetime64_any_dtype(self.sp_values.dtype):
            if fill_value is NaT:
                fill_value = np.datetime64('NaT')
        try:
            dtype = np.result_type(self.sp_values.dtype, type(fill_value))
        except TypeError:
            dtype = object
    out = np.full(self.shape, fill_value, dtype=dtype)
    out[self.sp_index.to_int_index().indices] = self.sp_values
    return out