def test_combine_scalar(self):
    s = pd.Series([i * 10 for i in range(5)])
    result = s.combine(3, lambda x, y: x + y)
    expected = pd.Series([i * 10 + 3 for i in range(5)])
    tm.assert_series_equal(result, expected)
    result = s.combine(22, lambda x, y: min(x, y))
    expected = pd.Series([min(i * 10, 22) for i in range(5)])
    tm.assert_series_equal(result, expected)