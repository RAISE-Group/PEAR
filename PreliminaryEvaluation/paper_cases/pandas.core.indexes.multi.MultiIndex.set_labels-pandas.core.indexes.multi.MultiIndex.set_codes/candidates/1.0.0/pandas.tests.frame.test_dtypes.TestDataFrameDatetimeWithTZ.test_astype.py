def test_astype(self, timezone_frame):
    expected = np.array([[Timestamp('2013-01-01 00:00:00'), Timestamp('2013-01-02 00:00:00'), Timestamp('2013-01-03 00:00:00')], [Timestamp('2013-01-01 00:00:00-0500', tz='US/Eastern'), pd.NaT, Timestamp('2013-01-03 00:00:00-0500', tz='US/Eastern')], [Timestamp('2013-01-01 00:00:00+0100', tz='CET'), pd.NaT, Timestamp('2013-01-03 00:00:00+0100', tz='CET')]], dtype=object).T
    expected = DataFrame(expected, index=timezone_frame.index, columns=timezone_frame.columns, dtype=object)
    result = timezone_frame.astype(object)
    tm.assert_frame_equal(result, expected)
    result = timezone_frame.astype('datetime64[ns]')
    expected = DataFrame({'A': date_range('20130101', periods=3), 'B': date_range('20130101', periods=3, tz='US/Eastern').tz_convert('UTC').tz_localize(None), 'C': date_range('20130101', periods=3, tz='CET').tz_convert('UTC').tz_localize(None)})
    expected.iloc[1, 1] = pd.NaT
    expected.iloc[1, 2] = pd.NaT
    tm.assert_frame_equal(result, expected)