def test_read_timezone_information(self):
    result = read_json('{"2019-01-01T11:00:00.000Z":88}', typ='series', orient='index')
    expected = Series([88], index=DatetimeIndex(['2019-01-01 11:00:00'], tz='UTC'))
    tm.assert_series_equal(result, expected)