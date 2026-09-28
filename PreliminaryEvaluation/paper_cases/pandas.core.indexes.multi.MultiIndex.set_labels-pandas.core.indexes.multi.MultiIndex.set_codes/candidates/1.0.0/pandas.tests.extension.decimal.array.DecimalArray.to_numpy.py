def to_numpy(self, dtype=None, copy=False, na_value=no_default, decimals=None):
    result = np.asarray(self, dtype=dtype)
    if decimals is not None:
        result = np.asarray([round(x, decimals) for x in result])
    return result