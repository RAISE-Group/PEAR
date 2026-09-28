def test_replace_mixed_types_with_string(self):
    s = pd.Series([1, 2, 3, '4', 4, 5])
    result = s.replace([2, '4'], np.nan)
    expected = pd.Series([1, np.nan, 3, np.nan, 4, 5])
    tm.assert_series_equal(expected, result)