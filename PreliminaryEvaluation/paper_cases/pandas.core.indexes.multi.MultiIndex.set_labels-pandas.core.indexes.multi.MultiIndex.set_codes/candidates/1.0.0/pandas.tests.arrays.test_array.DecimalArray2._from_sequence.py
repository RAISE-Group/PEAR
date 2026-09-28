@classmethod
def _from_sequence(cls, scalars, dtype=None, copy=False):
    if isinstance(scalars, (pd.Series, pd.Index)):
        raise TypeError
    return super()._from_sequence(scalars, dtype=dtype, copy=copy)