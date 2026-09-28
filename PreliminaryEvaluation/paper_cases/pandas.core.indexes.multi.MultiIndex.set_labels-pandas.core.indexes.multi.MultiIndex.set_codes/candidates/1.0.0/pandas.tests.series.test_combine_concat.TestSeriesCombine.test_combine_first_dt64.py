def test_combine_first_dt64(self):
    from pandas.core.tools.datetimes import to_datetime
    s0 = to_datetime(Series(['2010', np.NaN]))
    s1 = to_datetime(Series([np.NaN, '2011']))
    rs = s0.combine_first(s1)
    xp = to_datetime(Series(['2010', '2011']))
    tm.assert_series_equal(rs, xp)
    s0 = to_datetime(Series(['2010', np.NaN]))
    s1 = Series([np.NaN, '2011'])
    rs = s0.combine_first(s1)
    xp = Series([datetime(2010, 1, 1), '2011'])
    tm.assert_series_equal(rs, xp)