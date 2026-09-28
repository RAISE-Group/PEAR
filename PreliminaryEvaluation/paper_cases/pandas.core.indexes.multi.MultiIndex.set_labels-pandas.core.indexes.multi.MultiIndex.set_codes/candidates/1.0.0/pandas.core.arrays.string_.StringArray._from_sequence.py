@classmethod
def _from_sequence(cls, scalars, dtype=None, copy=False):
    if dtype:
        assert dtype == 'string'
    result = np.asarray(scalars, dtype='object')
    if copy and result is scalars:
        result = result.copy()
    na_values = isna(result)
    if na_values.any():
        if result is scalars:
            result = result.copy()
        result[na_values] = StringDtype.na_value
    return cls(result)