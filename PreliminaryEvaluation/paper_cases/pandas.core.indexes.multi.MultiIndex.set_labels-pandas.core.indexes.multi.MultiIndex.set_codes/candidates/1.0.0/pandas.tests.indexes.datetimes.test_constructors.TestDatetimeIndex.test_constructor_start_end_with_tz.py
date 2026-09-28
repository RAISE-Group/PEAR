@pytest.mark.parametrize('tz', [None, 'America/Los_Angeles', pytz.timezone('America/Los_Angeles'), Timestamp('2000', tz='America/Los_Angeles').tz])
def test_constructor_start_end_with_tz(self, tz):
    start = Timestamp('2013-01-01 06:00:00', tz='America/Los_Angeles')
    end = Timestamp('2013-01-02 06:00:00', tz='America/Los_Angeles')
    result = date_range(freq='D', start=start, end=end, tz=tz)
    expected = DatetimeIndex(['2013-01-01 06:00:00', '2013-01-02 06:00:00'], tz='America/Los_Angeles')
    tm.assert_index_equal(result, expected)
    assert pytz.timezone('America/Los_Angeles') is result.tz