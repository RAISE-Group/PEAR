def test_ops_series_timedelta(self):
    ser = pd.Series([pd.Period('2015-01-01', freq='D'), pd.Period('2015-01-02', freq='D')], name='xxx')
    assert ser.dtype == 'Period[D]'
    expected = pd.Series([pd.Period('2015-01-02', freq='D'), pd.Period('2015-01-03', freq='D')], name='xxx')
    result = ser + pd.Timedelta('1 days')
    tm.assert_series_equal(result, expected)
    result = pd.Timedelta('1 days') + ser
    tm.assert_series_equal(result, expected)
    result = ser + pd.tseries.offsets.Day()
    tm.assert_series_equal(result, expected)
    result = pd.tseries.offsets.Day() + ser
    tm.assert_series_equal(result, expected)