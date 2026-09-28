@pytest.mark.parametrize('cache', [True, False])
@pytest.mark.parametrize('date, dtype', [('2013-01-01 01:00:00', 'datetime64[ns]'), ('2013-01-01 01:00:00', 'datetime64[ns, UTC]')])
def test_to_datetime_utc_true_with_series_datetime_ns(self, cache, date, dtype):
    expected = pd.Series([pd.Timestamp('2013-01-01 01:00:00', tz='UTC')])
    result = pd.to_datetime(pd.Series([date], dtype=dtype), utc=True, cache=cache)
    tm.assert_series_equal(result, expected)