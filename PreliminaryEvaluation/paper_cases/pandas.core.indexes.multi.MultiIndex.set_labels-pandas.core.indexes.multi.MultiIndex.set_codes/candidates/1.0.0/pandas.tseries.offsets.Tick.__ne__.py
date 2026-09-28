def __ne__(self, other):
    if isinstance(other, str):
        from pandas.tseries.frequencies import to_offset
        try:
            other = to_offset(other)
        except ValueError:
            return True
    if isinstance(other, Tick):
        return self.delta != other.delta
    else:
        return True