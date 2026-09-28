def test_mode_sortwarning(self):
    expected = Series(['foo', np.nan])
    s = Series([1, 'foo', 'foo', np.nan, np.nan])
    with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
        result = s.mode(dropna=False)
        result = result.sort_values().reset_index(drop=True)
    tm.assert_series_equal(result, expected)