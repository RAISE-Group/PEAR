def _validate_dtype(self, dtype):
    """ validate the passed dtype """
    if dtype is not None:
        dtype = pandas_dtype(dtype)
        if dtype.kind == 'V':
            raise NotImplementedError(f'compound dtypes are not implemented in the {type(self).__name__} constructor')
    return dtype