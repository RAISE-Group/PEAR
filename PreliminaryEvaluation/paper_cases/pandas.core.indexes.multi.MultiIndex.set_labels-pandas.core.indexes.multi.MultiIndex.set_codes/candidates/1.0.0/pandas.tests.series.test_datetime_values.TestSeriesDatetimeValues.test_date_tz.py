def test_date_tz(self):
    rng = pd.DatetimeIndex(['2014-04-04 23:56', '2014-07-18 21:24', '2015-11-22 22:14'], tz='US/Eastern')
    s = Series(rng)
    expected = Series([date(2014, 4, 4), date(2014, 7, 18), date(2015, 11, 22)])
    tm.assert_series_equal(s.dt.date, expected)
    tm.assert_series_equal(s.apply(lambda x: x.date()), expected)