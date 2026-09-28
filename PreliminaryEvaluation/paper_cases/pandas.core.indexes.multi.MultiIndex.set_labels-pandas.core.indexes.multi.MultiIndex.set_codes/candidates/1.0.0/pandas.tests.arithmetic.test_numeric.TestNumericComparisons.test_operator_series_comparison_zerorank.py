def test_operator_series_comparison_zerorank(self):
    result = np.float64(0) > pd.Series([1, 2, 3])
    expected = 0.0 > pd.Series([1, 2, 3])
    tm.assert_series_equal(result, expected)
    result = pd.Series([1, 2, 3]) < np.float64(0)
    expected = pd.Series([1, 2, 3]) < 0.0
    tm.assert_series_equal(result, expected)
    result = np.array([0, 1, 2])[0] > pd.Series([0, 1, 2])
    expected = 0.0 > pd.Series([1, 2, 3])
    tm.assert_series_equal(result, expected)