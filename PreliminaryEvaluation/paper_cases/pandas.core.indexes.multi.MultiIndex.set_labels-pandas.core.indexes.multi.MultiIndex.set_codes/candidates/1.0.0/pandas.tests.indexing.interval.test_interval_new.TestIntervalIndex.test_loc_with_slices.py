def test_loc_with_slices(self):
    s = self.s
    expected = s.iloc[:3]
    result = s.loc[Interval(0, 1):Interval(2, 3)]
    tm.assert_series_equal(expected, result)
    result = s[Interval(0, 1):Interval(2, 3)]
    tm.assert_series_equal(expected, result)
    expected = s.iloc[3:]
    result = s.loc[Interval(3, 4):]
    tm.assert_series_equal(expected, result)
    result = s[Interval(3, 4):]
    tm.assert_series_equal(expected, result)
    msg = 'Interval objects are not currently supported'
    with pytest.raises(NotImplementedError, match=msg):
        s.loc[Interval(3, 6):]
    with pytest.raises(NotImplementedError, match=msg):
        s[Interval(3, 6):]
    with pytest.raises(NotImplementedError, match=msg):
        s.loc[Interval(3, 4, closed='left'):]
    with pytest.raises(NotImplementedError, match=msg):
        s[Interval(3, 4, closed='left'):]
    expected = s.iloc[:3]
    tm.assert_series_equal(expected, s.loc[:3])
    tm.assert_series_equal(expected, s.loc[:2.5])
    tm.assert_series_equal(expected, s.loc[0.1:2.5])
    tm.assert_series_equal(expected, s.loc[-1:3])
    tm.assert_series_equal(expected, s[:3])
    tm.assert_series_equal(expected, s[:2.5])
    tm.assert_series_equal(expected, s[0.1:2.5])
    with pytest.raises(ValueError):
        s[0:4:2]