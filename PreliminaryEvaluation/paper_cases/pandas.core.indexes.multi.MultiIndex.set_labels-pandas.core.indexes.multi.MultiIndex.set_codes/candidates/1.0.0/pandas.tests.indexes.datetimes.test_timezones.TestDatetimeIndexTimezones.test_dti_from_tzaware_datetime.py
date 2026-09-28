@pytest.mark.parametrize('tz', [pytz.timezone('US/Eastern'), gettz('US/Eastern')])
def test_dti_from_tzaware_datetime(self, tz):
    d = [datetime(2012, 8, 19, tzinfo=tz)]
    index = DatetimeIndex(d)
    assert timezones.tz_compare(index.tz, tz)