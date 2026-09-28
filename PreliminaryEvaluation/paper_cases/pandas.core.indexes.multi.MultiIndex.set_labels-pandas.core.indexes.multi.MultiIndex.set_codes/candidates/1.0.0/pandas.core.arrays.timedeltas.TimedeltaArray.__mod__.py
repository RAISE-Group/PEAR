def __mod__(self, other):
    if isinstance(other, (ABCSeries, ABCDataFrame, ABCIndexClass)):
        return NotImplemented
    other = lib.item_from_zerodim(other)
    if isinstance(other, (timedelta, np.timedelta64, Tick)):
        other = Timedelta(other)
    return self - self // other * other