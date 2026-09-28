def __rtruediv__(self, other):
    other = lib.item_from_zerodim(other)
    if isinstance(other, (ABCSeries, ABCDataFrame, ABCIndexClass)):
        return NotImplemented
    if isinstance(other, (timedelta, np.timedelta64, Tick)):
        other = Timedelta(other)
        if other is NaT:
            result = np.empty(self.shape, dtype=np.float64)
            result.fill(np.nan)
            return result
        return other / self._data
    elif lib.is_scalar(other):
        raise TypeError(f'Cannot divide {type(other).__name__} by {type(self).__name__}')
    if not hasattr(other, 'dtype'):
        other = np.array(other)
    if len(other) != len(self):
        raise ValueError('Cannot divide vectors with unequal lengths')
    elif is_timedelta64_dtype(other.dtype):
        return other / self._data
    elif is_object_dtype(other.dtype):
        result = [other[n] / self[n] for n in range(len(self))]
        return np.array(result)
    else:
        raise TypeError(f'Cannot divide {other.dtype} data by {type(self).__name__}')