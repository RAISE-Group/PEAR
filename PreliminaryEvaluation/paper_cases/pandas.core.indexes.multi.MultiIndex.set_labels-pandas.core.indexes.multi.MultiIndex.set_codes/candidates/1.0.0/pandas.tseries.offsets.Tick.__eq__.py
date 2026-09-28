def __eq__(self, other: Any) -> bool:
    if isinstance(other, str):
        from pandas.tseries.frequencies import to_offset
        try:
            other = to_offset(other)
        except ValueError:
            return False
    if isinstance(other, Tick):
        return self.delta == other.delta
    else:
        return False