def test_describe_empty_object(self):
    s = Series([None, None], dtype=object)
    result = s.describe()
    expected = Series([0, 0, np.nan, np.nan], dtype=object, index=['count', 'unique', 'top', 'freq'])
    tm.assert_series_equal(result, expected)
    result = s[:0].describe()
    tm.assert_series_equal(result, expected)
    assert np.isnan(result.iloc[2])
    assert np.isnan(result.iloc[3])