def __truediv__(self, other):
    other = lib.item_from_zerodim(other)
    if isinstance(other, (ABCSeries, ABCDataFrame, ABCIndexClass)):
        return NotImplemented
    if isinstance(other, (timedelta, np.timedelta64, Tick)):
        other = Timedelta(other)
        if other is NaT:
            result = np.empty(self.shape, dtype=np.float64)
            result.fill(np.nan)
            return result
        return self._data / other
    elif lib.is_scalar(other):
        result = self._data / other
        freq = None
        if self.freq is not None:
            freq = self.freq.delta / other
        return type(self)(result, freq=freq)
    if not hasattr(other, 'dtype'):
        other = np.array(other)
    if len(other) != len(self):
        raise ValueError('Cannot divide vectors with unequal lengths')
    elif is_timedelta64_dtype(other.dtype):
        return self._data / other
    elif is_object_dtype(other.dtype):
        result = [self[n] / other[n] for n in range(len(self))]
        result = np.array(result)
        return result
    else:
        result = self._data / other
        return type(self)(result)