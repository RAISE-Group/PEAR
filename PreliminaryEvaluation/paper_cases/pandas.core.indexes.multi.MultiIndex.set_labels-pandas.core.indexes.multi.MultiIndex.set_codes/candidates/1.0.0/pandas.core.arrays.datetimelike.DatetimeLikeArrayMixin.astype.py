def astype(self, dtype, copy=True):
    from pandas import Categorical
    dtype = pandas_dtype(dtype)
    if is_object_dtype(dtype):
        return self._box_values(self.asi8)
    elif is_string_dtype(dtype) and (not is_categorical_dtype(dtype)):
        return self._format_native_types()
    elif is_integer_dtype(dtype):
        values = self.asi8
        if is_unsigned_integer_dtype(dtype):
            values = values.view('uint64')
        if copy:
            values = values.copy()
        return values
    elif is_datetime_or_timedelta_dtype(dtype) and (not is_dtype_equal(self.dtype, dtype)) or is_float_dtype(dtype):
        msg = f'Cannot cast {type(self).__name__} to dtype {dtype}'
        raise TypeError(msg)
    elif is_categorical_dtype(dtype):
        return Categorical(self, dtype=dtype)
    else:
        return np.asarray(self, dtype=dtype)