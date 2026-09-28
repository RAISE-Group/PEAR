@pytest.mark.parametrize('cache', [True, False])
@pytest.mark.parametrize('dt_string, tz, dt_string_repr', [('2013-01-01 05:45+0545', pytz.FixedOffset(345), "Timestamp('2013-01-01 05:45:00+0545', tz='pytz.FixedOffset(345)')"), ('2013-01-01 05:30+0530', pytz.FixedOffset(330), "Timestamp('2013-01-01 05:30:00+0530', tz='pytz.FixedOffset(330)')")])
def test_parsers_timezone_minute_offsets_roundtrip(self, cache, dt_string, tz, dt_string_repr):
    base = to_datetime('2013-01-01 00:00:00', cache=cache)
    base = base.tz_localize('UTC').tz_convert(tz)
    dt_time = to_datetime(dt_string, cache=cache)
    assert base == dt_time
    assert dt_string_repr == repr(dt_time)