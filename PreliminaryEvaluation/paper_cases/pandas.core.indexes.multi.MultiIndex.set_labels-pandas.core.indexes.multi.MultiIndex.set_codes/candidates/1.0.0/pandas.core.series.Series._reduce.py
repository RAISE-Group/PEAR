def _reduce(self, op, name, axis=0, skipna=True, numeric_only=None, filter_type=None, **kwds):
    """
        Perform a reduction operation.

        If we have an ndarray as a value, then simply perform the operation,
        otherwise delegate to the object.
        """
    delegate = self._values
    if axis is not None:
        self._get_axis_number(axis)
    if isinstance(delegate, Categorical):
        return delegate._reduce(name, skipna=skipna, **kwds)
    elif isinstance(delegate, ExtensionArray):
        return delegate._reduce(name, skipna=skipna, **kwds)
    elif is_datetime64_dtype(delegate):
        delegate = DatetimeIndex(delegate)
    elif is_timedelta64_dtype(delegate) and hasattr(TimedeltaIndex, name):
        delegate = TimedeltaIndex(delegate)
    elif isinstance(delegate, np.ndarray):
        if numeric_only:
            raise NotImplementedError(f'Series.{name} does not implement numeric_only.')
        with np.errstate(all='ignore'):
            return op(delegate, skipna=skipna, **kwds)
    return delegate._reduce(op=op, name=name, axis=axis, skipna=skipna, numeric_only=numeric_only, filter_type=filter_type, **kwds)