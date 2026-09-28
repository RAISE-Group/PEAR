@pytest.mark.parametrize('utc', [True, None])
@pytest.mark.parametrize('format', ['%Y%m%d %H:%M:%S', None])
def test_to_datetime_cache_series(self, utc, format):
    date = '20130101 00:00:00'
    test_dates = [date] * 10 ** 5
    data = pd.Series(test_dates)
    result = pd.to_datetime(data, utc=utc, format=format, cache=True)
    expected = pd.to_datetime(data, utc=utc, format=format, cache=False)
    tm.assert_series_equal(result, expected)