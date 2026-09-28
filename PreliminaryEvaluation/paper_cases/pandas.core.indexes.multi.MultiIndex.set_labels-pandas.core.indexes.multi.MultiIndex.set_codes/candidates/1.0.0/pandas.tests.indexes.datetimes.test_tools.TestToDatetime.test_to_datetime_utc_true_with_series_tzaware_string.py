@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_utc_true_with_series_tzaware_string(self, cache):
    ts = '2013-01-01 00:00:00-01:00'
    expected_ts = '2013-01-01 01:00:00'
    data = pd.Series([ts] * 3)
    result = pd.to_datetime(data, utc=True, cache=cache)
    expected = pd.Series([pd.Timestamp(expected_ts, tz='utc')] * 3)
    tm.assert_series_equal(result, expected)