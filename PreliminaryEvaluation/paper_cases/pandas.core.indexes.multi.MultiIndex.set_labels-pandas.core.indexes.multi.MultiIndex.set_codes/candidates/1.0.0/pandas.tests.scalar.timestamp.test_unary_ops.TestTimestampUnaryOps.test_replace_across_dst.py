@pytest.mark.parametrize('tz, normalize', [(pytz.timezone('US/Eastern'), lambda x: x.tzinfo.normalize(x)), (gettz('US/Eastern'), lambda x: x)])
def test_replace_across_dst(self, tz, normalize):
    ts_naive = Timestamp('2017-12-03 16:03:30')
    ts_aware = conversion.localize_pydatetime(ts_naive, tz)
    assert ts_aware == normalize(ts_aware)
    ts2 = ts_aware.replace(month=6)
    assert (ts2.hour, ts2.minute) == (ts_aware.hour, ts_aware.minute)
    ts2b = normalize(ts2)
    assert ts2 == ts2b