@classmethod
def _from_factorized(cls, values, original):
    if len(values) == 0:
        values = values.astype(original.dtype.subtype)
    return cls(values, closed=original.closed)