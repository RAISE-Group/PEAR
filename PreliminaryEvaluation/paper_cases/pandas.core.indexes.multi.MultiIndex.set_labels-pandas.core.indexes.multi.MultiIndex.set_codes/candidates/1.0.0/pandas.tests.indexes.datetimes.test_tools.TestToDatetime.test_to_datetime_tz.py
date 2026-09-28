@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_tz(self, cache):
    arr = [pd.Timestamp('2013-01-01 13:00:00-0800', tz='US/Pacific'), pd.Timestamp('2013-01-02 14:00:00-0800', tz='US/Pacific')]
    result = pd.to_datetime(arr, cache=cache)
    expected = DatetimeIndex(['2013-01-01 13:00:00', '2013-01-02 14:00:00'], tz='US/Pacific')
    tm.assert_index_equal(result, expected)
    arr = [pd.Timestamp('2013-01-01 13:00:00', tz='US/Pacific'), pd.Timestamp('2013-01-02 14:00:00', tz='US/Eastern')]
    msg = 'Tz-aware datetime.datetime cannot be converted to datetime64 unless utc=True'
    with pytest.raises(ValueError, match=msg):
        pd.to_datetime(arr, cache=cache)