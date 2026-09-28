def _assert_setitem_index_conversion(self, original_series, loc_key, expected_index, expected_dtype):
    """ test index's coercion triggered by assign key """
    temp = original_series.copy()
    temp[loc_key] = 5
    exp = pd.Series([1, 2, 3, 4, 5], index=expected_index)
    tm.assert_series_equal(temp, exp)
    assert temp.index.dtype == expected_dtype
    temp = original_series.copy()
    temp.loc[loc_key] = 5
    exp = pd.Series([1, 2, 3, 4, 5], index=expected_index)
    tm.assert_series_equal(temp, exp)
    assert temp.index.dtype == expected_dtype