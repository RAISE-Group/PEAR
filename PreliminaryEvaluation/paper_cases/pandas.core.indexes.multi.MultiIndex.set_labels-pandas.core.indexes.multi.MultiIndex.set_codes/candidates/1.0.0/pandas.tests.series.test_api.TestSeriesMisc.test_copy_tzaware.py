def test_copy_tzaware(self):
    expected = Series([Timestamp('2012/01/01', tz='UTC')])
    expected2 = Series([Timestamp('1999/01/01', tz='UTC')])
    for deep in [None, False, True]:
        s = Series([Timestamp('2012/01/01', tz='UTC')])
        if deep is None:
            s2 = s.copy()
        else:
            s2 = s.copy(deep=deep)
        s2[0] = pd.Timestamp('1999/01/01', tz='UTC')
        if deep is None or deep is True:
            tm.assert_series_equal(s2, expected2)
            tm.assert_series_equal(s, expected)
        else:
            tm.assert_series_equal(s2, expected2)
            tm.assert_series_equal(s, expected2)