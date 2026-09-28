def test_between(self):
    series = Series(date_range('1/1/2000', periods=10))
    left, right = series[[2, 7]]
    result = series.between(left, right)
    expected = (series >= left) & (series <= right)
    tm.assert_series_equal(result, expected)