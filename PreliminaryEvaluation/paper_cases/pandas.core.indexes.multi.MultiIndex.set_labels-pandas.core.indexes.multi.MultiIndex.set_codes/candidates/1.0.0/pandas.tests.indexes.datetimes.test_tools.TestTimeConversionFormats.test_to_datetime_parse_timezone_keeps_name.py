def test_to_datetime_parse_timezone_keeps_name(self):
    fmt = '%Y-%m-%d %H:%M:%S %z'
    arg = pd.Index(['2010-01-01 12:00:00 Z'], name='foo')
    result = pd.to_datetime(arg, format=fmt)
    expected = pd.DatetimeIndex(['2010-01-01 12:00:00'], tz='UTC', name='foo')
    tm.assert_index_equal(result, expected)