def astype(self, dtype, copy: bool=False, errors: str='raise'):
    """
        Coerce to the new dtype.

        Parameters
        ----------
        dtype : str, dtype convertible
        copy : bool, default False
            copy if indicated
        errors : str, {'raise', 'ignore'}, default 'ignore'
            - ``raise`` : allow exceptions to be raised
            - ``ignore`` : suppress exceptions. On error return original object

        Returns
        -------
        Block
        """
    errors_legal_values = ('raise', 'ignore')
    if errors not in errors_legal_values:
        invalid_arg = f"Expected value of kwarg 'errors' to be one of {list(errors_legal_values)}. Supplied value is '{errors}'"
        raise ValueError(invalid_arg)
    if inspect.isclass(dtype) and issubclass(dtype, ExtensionDtype):
        msg = f"Expected an instance of {dtype.__name__}, but got the class instead. Try instantiating 'dtype'."
        raise TypeError(msg)
    if self.is_categorical_astype(dtype):
        if is_categorical_dtype(self.values):
            return self.make_block(self.values.astype(dtype, copy=copy))
        return self.make_block(Categorical(self.values, dtype=dtype))
    dtype = pandas_dtype(dtype)
    if is_dtype_equal(self.dtype, dtype):
        if copy:
            return self.copy()
        return self
    if self.is_extension:
        values = self.values.astype(dtype)
    else:
        if issubclass(dtype.type, str):
            if self.is_datelike:
                values = self.to_native_types()
            else:
                values = self.get_values()
        else:
            values = self.get_values(dtype=dtype)
        vals1d = values.ravel()
        try:
            values = astype_nansafe(vals1d, dtype, copy=True)
        except (ValueError, TypeError):
            if errors == 'raise':
                raise
            newb = self.copy() if copy else self
            return newb
    if isinstance(values, np.ndarray):
        values = values.reshape(self.shape)
    newb = make_block(values, placement=self.mgr_locs, ndim=self.ndim)
    if newb.is_numeric and self.is_numeric:
        if newb.shape != self.shape:
            raise TypeError(f'cannot set astype for copy = [{copy}] for dtype ({self.dtype.name} [{self.shape}]) to different shape ({newb.dtype.name} [{newb.shape}])')
    return newb