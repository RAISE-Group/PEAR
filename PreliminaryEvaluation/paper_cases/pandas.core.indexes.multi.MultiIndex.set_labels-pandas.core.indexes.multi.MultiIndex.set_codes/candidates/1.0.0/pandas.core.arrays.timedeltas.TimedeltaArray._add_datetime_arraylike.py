def _add_datetime_arraylike(self, other):
    """
        Add DatetimeArray/Index or ndarray[datetime64] to TimedeltaArray.
        """
    if isinstance(other, np.ndarray):
        from pandas.core.arrays import DatetimeArray
        other = DatetimeArray(other)
    return other + self