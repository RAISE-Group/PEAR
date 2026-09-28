def test_loc_with_scalar(self):
    s = self.s
    assert s.loc[1] == 0
    assert s.loc[1.5] == 1
    assert s.loc[2] == 1
    assert s[1] == 0
    assert s[1.5] == 1
    assert s[2] == 1
    expected = s.iloc[1:4]
    tm.assert_series_equal(expected, s.loc[[1.5, 2.5, 3.5]])
    tm.assert_series_equal(expected, s.loc[[2, 3, 4]])
    tm.assert_series_equal(expected, s.loc[[1.5, 3, 4]])
    expected = s.iloc[[1, 1, 2, 1]]
    tm.assert_series_equal(expected, s.loc[[1.5, 2, 2.5, 1.5]])
    expected = s.iloc[2:5]
    tm.assert_series_equal(expected, s.loc[s >= 2])