def _assert_setitem_series_conversion(self, original_series, loc_value, expected_series, expected_dtype):
    """ test series value's coercion triggered by assignment """
    temp = original_series.copy()
    temp[1] = loc_value
    tm.assert_series_equal(temp, expected_series)
    assert temp.dtype == expected_dtype