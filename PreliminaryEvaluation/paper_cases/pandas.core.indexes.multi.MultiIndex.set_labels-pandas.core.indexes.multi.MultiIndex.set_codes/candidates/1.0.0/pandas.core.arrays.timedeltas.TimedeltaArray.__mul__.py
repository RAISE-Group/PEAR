def __mul__(self, other):
    other = lib.item_from_zerodim(other)
    if isinstance(other, (ABCDataFrame, ABCSeries, ABCIndexClass)):
        return NotImplemented
    if is_scalar(other):
        result = self._data * other
        freq = None
        if self.freq is not None and (not isna(other)):
            freq = self.freq * other
        return type(self)(result, freq=freq)
    if not hasattr(other, 'dtype'):
        other = np.array(other)
    if len(other) != len(self) and (not is_timedelta64_dtype(other)):
        raise ValueError('Cannot multiply with unequal lengths')
    if is_object_dtype(other.dtype):
        result = [self[n] * other[n] for n in range(len(self))]
        result = np.array(result)
        return type(self)(result)
    result = self._data * other
    return type(self)(result)