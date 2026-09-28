def _add_datetimelike_scalar(self, other):
    from pandas.core.arrays import DatetimeArray
    assert other is not NaT
    other = Timestamp(other)
    if other is NaT:
        result = self.asi8.view('m8[ms]') + NaT.to_datetime64()
        return DatetimeArray(result)
    i8 = self.asi8
    result = checked_add_with_arr(i8, other.value, arr_mask=self._isnan)
    result = self._maybe_mask_results(result)
    dtype = DatetimeTZDtype(tz=other.tz) if other.tz else _NS_DTYPE
    return DatetimeArray(result, dtype=dtype, freq=self.freq)