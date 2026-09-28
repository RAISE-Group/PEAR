@classmethod
def _simple_new(cls, values, name=None, freq=None, tz=None, dtype=None):
    """
        We require the we have a dtype compat for the values
        if we are passed a non-dtype compat, then coerce using the constructor
        """
    if isinstance(values, DatetimeArray):
        if tz:
            tz = validate_tz_from_dtype(dtype, tz)
            dtype = DatetimeTZDtype(tz=tz)
        elif dtype is None:
            dtype = _NS_DTYPE
        values = DatetimeArray(values, freq=freq, dtype=dtype)
        tz = values.tz
        freq = values.freq
        values = values._data
    if isinstance(values, DatetimeIndex):
        values = values._data
    dtype = tz_to_dtype(tz)
    dtarr = DatetimeArray._simple_new(values, freq=freq, dtype=dtype)
    assert isinstance(dtarr, DatetimeArray)
    result = object.__new__(cls)
    result._data = dtarr
    result.name = name
    result._no_setting_name = False
    result._index_data = dtarr._data
    result._reset_identity()
    return result