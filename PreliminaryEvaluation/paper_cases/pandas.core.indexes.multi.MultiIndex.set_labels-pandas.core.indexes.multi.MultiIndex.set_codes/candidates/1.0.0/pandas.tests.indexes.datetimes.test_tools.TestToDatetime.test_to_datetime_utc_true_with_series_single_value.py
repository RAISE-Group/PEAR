@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_utc_true_with_series_single_value(self, cache):
    ts = 1.5e+18
    result = pd.to_datetime(pd.Series([ts]), utc=True, cache=cache)
    expected = pd.Series([pd.Timestamp(ts, tz='utc')])
    tm.assert_series_equal(result, expected)