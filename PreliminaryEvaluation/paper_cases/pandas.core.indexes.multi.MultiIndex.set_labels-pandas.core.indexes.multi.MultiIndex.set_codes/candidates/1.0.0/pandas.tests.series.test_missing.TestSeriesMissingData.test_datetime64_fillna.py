def test_datetime64_fillna(self):
    s = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130102'), Timestamp('20130103 9:01:01')])
    s[2] = np.nan
    result = s.fillna(Timestamp('20130104'))
    expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130104'), Timestamp('20130103 9:01:01')])
    tm.assert_series_equal(result, expected)
    result = s.fillna(NaT)
    expected = s
    tm.assert_series_equal(result, expected)
    result = s.ffill()
    expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130103 9:01:01')])
    tm.assert_series_equal(result, expected)
    result = s.bfill()
    expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130103 9:01:01'), Timestamp('20130103 9:01:01')])
    tm.assert_series_equal(result, expected)
    s = Series([pd.NaT, pd.NaT, '2013-08-05 15:30:00.000001'])
    expected = Series(['2013-08-05 15:30:00.000001', '2013-08-05 15:30:00.000001', '2013-08-05 15:30:00.000001'], dtype='M8[ns]')
    result = s.fillna(method='backfill')
    tm.assert_series_equal(result, expected)