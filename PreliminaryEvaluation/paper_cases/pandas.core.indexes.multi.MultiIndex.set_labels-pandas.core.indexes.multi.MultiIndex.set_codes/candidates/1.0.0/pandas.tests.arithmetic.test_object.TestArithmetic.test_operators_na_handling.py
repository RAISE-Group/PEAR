def test_operators_na_handling(self):
    ser = Series(['foo', 'bar', 'baz', np.nan])
    result = 'prefix_' + ser
    expected = pd.Series(['prefix_foo', 'prefix_bar', 'prefix_baz', np.nan])
    tm.assert_series_equal(result, expected)
    result = ser + '_suffix'
    expected = pd.Series(['foo_suffix', 'bar_suffix', 'baz_suffix', np.nan])
    tm.assert_series_equal(result, expected)