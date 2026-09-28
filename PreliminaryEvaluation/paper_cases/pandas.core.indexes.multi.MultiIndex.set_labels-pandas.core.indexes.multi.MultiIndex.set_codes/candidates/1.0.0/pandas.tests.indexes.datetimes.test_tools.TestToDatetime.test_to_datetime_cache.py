@pytest.mark.parametrize('utc', [True, None])
@pytest.mark.parametrize('format', ['%Y%m%d %H:%M:%S', None])
@pytest.mark.parametrize('constructor', [list, tuple, np.array, pd.Index, deque])
def test_to_datetime_cache(self, utc, format, constructor):
    date = '20130101 00:00:00'
    test_dates = [date] * 10 ** 5
    data = constructor(test_dates)
    result = pd.to_datetime(data, utc=utc, format=format, cache=True)
    expected = pd.to_datetime(data, utc=utc, format=format, cache=False)
    tm.assert_index_equal(result, expected)