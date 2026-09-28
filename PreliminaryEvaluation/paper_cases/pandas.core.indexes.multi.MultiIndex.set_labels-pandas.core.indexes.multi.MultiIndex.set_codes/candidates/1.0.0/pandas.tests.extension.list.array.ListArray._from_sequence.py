@classmethod
def _from_sequence(cls, scalars, dtype=None, copy=False):
    data = np.empty(len(scalars), dtype=object)
    data[:] = scalars
    return cls(data)