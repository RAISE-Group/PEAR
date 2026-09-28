@classmethod
def _get_atom(cls, values: Union[np.ndarray, ABCExtensionArray]) -> 'Col':
    """
        Get an appropriately typed and shaped pytables.Col object for values.
        """
    dtype = values.dtype
    itemsize = dtype.itemsize
    shape = values.shape
    if values.ndim == 1:
        shape = (1, values.size)
    if is_categorical_dtype(dtype):
        codes = values.codes
        atom = cls.get_atom_data(shape, kind=codes.dtype.name)
    elif is_datetime64_dtype(dtype) or is_datetime64tz_dtype(dtype):
        atom = cls.get_atom_datetime64(shape)
    elif is_timedelta64_dtype(dtype):
        atom = cls.get_atom_timedelta64(shape)
    elif is_complex_dtype(dtype):
        atom = _tables().ComplexCol(itemsize=itemsize, shape=shape[0])
    elif is_string_dtype(dtype):
        atom = cls.get_atom_string(shape, itemsize)
    else:
        atom = cls.get_atom_data(shape, kind=dtype.name)
    return atom