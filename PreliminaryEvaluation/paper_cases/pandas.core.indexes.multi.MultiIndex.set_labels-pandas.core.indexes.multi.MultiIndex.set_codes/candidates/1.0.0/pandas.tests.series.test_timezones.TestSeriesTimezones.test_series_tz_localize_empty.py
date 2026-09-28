@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_series_tz_localize_empty(self, tzstr):
    ser = Series(dtype=object)
    ser2 = ser.tz_localize('utc')
    assert ser2.index.tz == pytz.utc
    ser2 = ser.tz_localize(tzstr)
    timezones.tz_compare(ser2.index.tz, timezones.maybe_get_tz(tzstr))