def max(self, axis=None, skipna=True, *args, **kwargs):
    """
        Return the maximum value of the Array or maximum along
        an axis.

        See Also
        --------
        numpy.ndarray.max
        Index.max : Return the maximum value in an Index.
        Series.max : Return the maximum value in a Series.
        """
    nv.validate_max(args, kwargs)
    nv.validate_minmax_axis(axis)
    mask = self.isna()
    if skipna:
        values = self[~mask].asi8
    elif mask.any():
        return NaT
    else:
        values = self.asi8
    if not len(values):
        return NaT
    result = nanops.nanmax(values, skipna=skipna)
    return self._box_func(result)