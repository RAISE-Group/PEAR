def test_between(self):
    left, right = self.series[[2, 7]]
    result = self.series.between(left, right)
    expected = (self.series >= left) & (self.series <= right)
    tm.assert_series_equal(result, expected)