def test_dropna(self):
    tm.assert_series_equal(Series([True, True, False]).value_counts(dropna=True), Series([2, 1], index=[True, False]))
    tm.assert_series_equal(Series([True, True, False]).value_counts(dropna=False), Series([2, 1], index=[True, False]))
    tm.assert_series_equal(Series([True, True, False, None]).value_counts(dropna=True), Series([2, 1], index=[True, False]))
    tm.assert_series_equal(Series([True, True, False, None]).value_counts(dropna=False), Series([2, 1, 1], index=[True, False, np.nan]))
    tm.assert_series_equal(Series([10.3, 5.0, 5.0]).value_counts(dropna=True), Series([2, 1], index=[5.0, 10.3]))
    tm.assert_series_equal(Series([10.3, 5.0, 5.0]).value_counts(dropna=False), Series([2, 1], index=[5.0, 10.3]))
    tm.assert_series_equal(Series([10.3, 5.0, 5.0, None]).value_counts(dropna=True), Series([2, 1], index=[5.0, 10.3]))
    if not compat.is_platform_32bit():
        result = Series([10.3, 5.0, 5.0, None]).value_counts(dropna=False)
        expected = Series([2, 1, 1], index=[5.0, 10.3, np.nan])
        tm.assert_series_equal(result, expected)