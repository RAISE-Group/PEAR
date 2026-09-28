@td.skip_if_windows
def test_tz_convert_utc_with_system_utc(self):
    ts = Timestamp('2001-01-05 11:56', tz=timezones.maybe_get_tz('dateutil/UTC'))
    assert ts == ts.tz_convert(dateutil.tz.tzutc())
    ts = Timestamp('2001-01-05 11:56', tz=timezones.maybe_get_tz('dateutil/UTC'))
    assert ts == ts.tz_convert(dateutil.tz.tzutc())