def test_getitem_with_scalar(self):
    s = self.s
    expected = s.iloc[:3]
    tm.assert_series_equal(expected, s[:3])
    tm.assert_series_equal(expected, s[:2.5])
    tm.assert_series_equal(expected, s[0.1:2.5])
    expected = s.iloc[1:4]
    tm.assert_series_equal(expected, s[[1.5, 2.5, 3.5]])
    tm.assert_series_equal(expected, s[[2, 3, 4]])
    tm.assert_series_equal(expected, s[[1.5, 3, 4]])
    expected = s.iloc[2:5]
    tm.assert_series_equal(expected, s[s >= 2])