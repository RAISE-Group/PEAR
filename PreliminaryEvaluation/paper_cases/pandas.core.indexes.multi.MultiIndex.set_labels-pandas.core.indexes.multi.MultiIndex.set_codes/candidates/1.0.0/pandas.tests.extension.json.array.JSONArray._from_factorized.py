@classmethod
def _from_factorized(cls, values, original):
    return cls([UserDict(x) for x in values if x != ()])