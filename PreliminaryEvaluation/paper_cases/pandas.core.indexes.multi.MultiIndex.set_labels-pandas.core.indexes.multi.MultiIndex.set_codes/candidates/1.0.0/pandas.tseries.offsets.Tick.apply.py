def apply(self, other):
    if isinstance(other, Timestamp):
        result = other.__add__(self)
        if result is NotImplemented:
            raise OverflowError
        return result
    elif isinstance(other, (datetime, np.datetime64, date)):
        return as_timestamp(other) + self
    if isinstance(other, timedelta):
        return other + self.delta
    elif isinstance(other, type(self)):
        return type(self)(self.n + other.n)
    raise ApplyTypeError(f'Unhandled type: {type(other).__name__}')