def test_mixed_timezone_series_ops_object(self):
    ser = pd.Series([pd.Timestamp('2015-01-01', tz='US/Eastern'), pd.Timestamp('2015-01-01', tz='Asia/Tokyo')], name='xxx')
    assert ser.dtype == object
    exp = pd.Series([pd.Timestamp('2015-01-02', tz='US/Eastern'), pd.Timestamp('2015-01-02', tz='Asia/Tokyo')], name='xxx')
    tm.assert_series_equal(ser + pd.Timedelta('1 days'), exp)
    tm.assert_series_equal(pd.Timedelta('1 days') + ser, exp)
    ser2 = pd.Series([pd.Timestamp('2015-01-03', tz='US/Eastern'), pd.Timestamp('2015-01-05', tz='Asia/Tokyo')], name='xxx')
    assert ser2.dtype == object
    exp = pd.Series([pd.Timedelta('2 days'), pd.Timedelta('4 days')], name='xxx')
    tm.assert_series_equal(ser2 - ser, exp)
    tm.assert_series_equal(ser - ser2, -exp)
    ser = pd.Series([pd.Timedelta('01:00:00'), pd.Timedelta('02:00:00')], name='xxx', dtype=object)
    assert ser.dtype == object
    exp = pd.Series([pd.Timedelta('01:30:00'), pd.Timedelta('02:30:00')], name='xxx')
    tm.assert_series_equal(ser + pd.Timedelta('00:30:00'), exp)
    tm.assert_series_equal(pd.Timedelta('00:30:00') + ser, exp)