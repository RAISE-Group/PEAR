@pytest.mark.parametrize('cache', [True, False])
@pytest.mark.parametrize('init_constructor, end_constructor, test_method', [(Index, DatetimeIndex, tm.assert_index_equal), (list, DatetimeIndex, tm.assert_index_equal), (np.array, DatetimeIndex, tm.assert_index_equal), (Series, Series, tm.assert_series_equal)])
def test_to_datetime_utc_true(self, cache, init_constructor, end_constructor, test_method):
    data = ['20100102 121314', '20100102 121315']
    expected_data = [pd.Timestamp('2010-01-02 12:13:14', tz='utc'), pd.Timestamp('2010-01-02 12:13:15', tz='utc')]
    result = pd.to_datetime(init_constructor(data), format='%Y%m%d %H%M%S', utc=True, cache=cache)
    expected = end_constructor(expected_data)
    test_method(result, expected)
    for scalar, expected in zip(data, expected_data):
        result = pd.to_datetime(scalar, format='%Y%m%d %H%M%S', utc=True, cache=cache)
        assert result == expected