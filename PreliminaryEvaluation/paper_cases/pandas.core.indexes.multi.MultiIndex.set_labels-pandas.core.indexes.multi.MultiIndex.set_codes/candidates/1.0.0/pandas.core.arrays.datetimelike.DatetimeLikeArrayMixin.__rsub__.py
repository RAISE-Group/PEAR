def __rsub__(self, other):
    if is_datetime64_any_dtype(other) and is_timedelta64_dtype(self.dtype):
        if lib.is_scalar(other):
            return Timestamp(other) - self
        if not isinstance(other, DatetimeLikeArrayMixin):
            from pandas.core.arrays import DatetimeArray
            other = DatetimeArray(other)
        return other - self
    elif is_datetime64_any_dtype(self.dtype) and hasattr(other, 'dtype') and (not is_datetime64_any_dtype(other.dtype)):
        raise TypeError(f'cannot subtract {type(self).__name__} from {type(other).__name__}')
    elif is_period_dtype(self.dtype) and is_timedelta64_dtype(other):
        raise TypeError(f'cannot subtract {type(self).__name__} from {other.dtype}')
    elif is_timedelta64_dtype(self.dtype):
        if lib.is_integer(other) or is_integer_dtype(other):
            return -(self - other)
        return -self + other
    return -(self - other)