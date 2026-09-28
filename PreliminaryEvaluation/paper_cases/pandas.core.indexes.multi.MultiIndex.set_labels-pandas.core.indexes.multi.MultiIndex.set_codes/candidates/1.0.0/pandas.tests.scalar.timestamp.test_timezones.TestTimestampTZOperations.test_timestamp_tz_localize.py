@pytest.mark.parametrize('tz', [pytz.timezone('US/Eastern'), gettz('US/Eastern'), 'US/Eastern', 'dateutil/US/Eastern'])
def test_timestamp_tz_localize(self, tz):
    stamp = Timestamp('3/11/2012 04:00')
    result = stamp.tz_localize(tz)
    expected = Timestamp('3/11/2012 04:00', tz=tz)
    assert result.hour == expected.hour
    assert result == expected