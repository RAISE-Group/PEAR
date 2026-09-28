def test_pct_change_with_duplicate_axis(self):
    common_idx = date_range('2019-11-14', periods=5, freq='D')
    result = Series(range(5), common_idx).pct_change(freq='B')
    expected = Series([np.NaN, np.inf, np.NaN, np.NaN, 3.0], common_idx)
    tm.assert_series_equal(result, expected)