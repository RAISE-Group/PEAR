def test_with_local_timezone_dateutil(self):
    local_timezone = 'dateutil/America/Los_Angeles'
    start = datetime(year=2013, month=11, day=1, hour=0, minute=0, tzinfo=dateutil.tz.tzutc())
    end = datetime(year=2013, month=11, day=2, hour=0, minute=0, tzinfo=dateutil.tz.tzutc())
    index = pd.date_range(start, end, freq='H', name='idx')
    series = Series(1, index=index)
    series = series.tz_convert(local_timezone)
    result = series.resample('D', kind='period').mean()
    expected_index = pd.period_range(start=start, end=end, freq='D', name='idx') - offsets.Day()
    expected = Series(1, index=expected_index)
    tm.assert_series_equal(result, expected)