def test_iloc_setitem_pandas_object(self):
    s_orig = Series([0, 1, 2, 3])
    expected = Series([0, -1, -2, 3])
    s = s_orig.copy()
    s.iloc[Series([1, 2])] = [-1, -2]
    tm.assert_series_equal(s, expected)
    s = s_orig.copy()
    s.iloc[pd.Index([1, 2])] = [-1, -2]
    tm.assert_series_equal(s, expected)