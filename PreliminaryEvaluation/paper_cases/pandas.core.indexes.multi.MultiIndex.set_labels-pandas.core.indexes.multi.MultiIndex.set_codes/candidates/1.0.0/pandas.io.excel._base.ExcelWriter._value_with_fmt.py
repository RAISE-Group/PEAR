def _value_with_fmt(self, val):
    """Convert numpy types to Python types for the Excel writers.

        Parameters
        ----------
        val : object
            Value to be written into cells

        Returns
        -------
        Tuple with the first element being the converted value and the second
            being an optional format
        """
    fmt = None
    if is_integer(val):
        val = int(val)
    elif is_float(val):
        val = float(val)
    elif is_bool(val):
        val = bool(val)
    elif isinstance(val, datetime):
        fmt = self.datetime_format
    elif isinstance(val, date):
        fmt = self.date_format
    elif isinstance(val, timedelta):
        val = val.total_seconds() / float(86400)
        fmt = '0'
    else:
        val = str(val)
    return (val, fmt)