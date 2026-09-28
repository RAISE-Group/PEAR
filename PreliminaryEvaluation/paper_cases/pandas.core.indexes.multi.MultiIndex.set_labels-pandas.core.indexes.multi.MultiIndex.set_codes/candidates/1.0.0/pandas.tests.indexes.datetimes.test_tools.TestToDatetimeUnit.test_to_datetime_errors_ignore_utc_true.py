def test_to_datetime_errors_ignore_utc_true(self):
    result = pd.to_datetime([1], unit='s', utc=True, errors='ignore')
    expected = DatetimeIndex(['1970-01-01 00:00:01'], tz='UTC')
    tm.assert_index_equal(result, expected)