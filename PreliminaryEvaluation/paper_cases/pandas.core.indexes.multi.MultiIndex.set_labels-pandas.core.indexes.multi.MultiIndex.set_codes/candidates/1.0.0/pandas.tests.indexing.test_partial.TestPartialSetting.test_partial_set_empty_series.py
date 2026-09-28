def test_partial_set_empty_series(self):
    s = Series(dtype=object)
    s.loc[1] = 1
    tm.assert_series_equal(s, Series([1], index=[1]))
    s.loc[3] = 3
    tm.assert_series_equal(s, Series([1, 3], index=[1, 3]))
    s = Series(dtype=object)
    s.loc[1] = 1.0
    tm.assert_series_equal(s, Series([1.0], index=[1]))
    s.loc[3] = 3.0
    tm.assert_series_equal(s, Series([1.0, 3.0], index=[1, 3]))
    s = Series(dtype=object)
    s.loc['foo'] = 1
    tm.assert_series_equal(s, Series([1], index=['foo']))
    s.loc['bar'] = 3
    tm.assert_series_equal(s, Series([1, 3], index=['foo', 'bar']))
    s.loc[3] = 4
    tm.assert_series_equal(s, Series([1, 3, 4], index=['foo', 'bar', 3]))