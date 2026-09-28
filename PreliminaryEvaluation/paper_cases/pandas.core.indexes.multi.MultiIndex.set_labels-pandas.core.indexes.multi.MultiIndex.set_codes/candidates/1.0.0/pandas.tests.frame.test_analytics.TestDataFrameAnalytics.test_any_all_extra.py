def test_any_all_extra(self):
    df = DataFrame({'A': [True, False, False], 'B': [True, True, False], 'C': [True, True, True]}, index=['a', 'b', 'c'])
    result = df[['A', 'B']].any(1)
    expected = Series([True, True, False], index=['a', 'b', 'c'])
    tm.assert_series_equal(result, expected)
    result = df[['A', 'B']].any(1, bool_only=True)
    tm.assert_series_equal(result, expected)
    result = df.all(1)
    expected = Series([True, False, False], index=['a', 'b', 'c'])
    tm.assert_series_equal(result, expected)
    result = df.all(1, bool_only=True)
    tm.assert_series_equal(result, expected)
    result = df.all(axis=None).item()
    assert result is False
    result = df.any(axis=None).item()
    assert result is True
    result = df[['C']].all(axis=None).item()
    assert result is True