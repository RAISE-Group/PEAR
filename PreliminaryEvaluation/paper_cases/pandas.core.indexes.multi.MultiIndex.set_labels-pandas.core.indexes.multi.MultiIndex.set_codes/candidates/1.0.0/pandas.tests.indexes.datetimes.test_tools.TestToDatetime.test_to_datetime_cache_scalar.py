def test_to_datetime_cache_scalar(self):
    date = '20130101 00:00:00'
    result = pd.to_datetime(date, cache=True)
    expected = pd.Timestamp('20130101 00:00:00')
    assert result == expected