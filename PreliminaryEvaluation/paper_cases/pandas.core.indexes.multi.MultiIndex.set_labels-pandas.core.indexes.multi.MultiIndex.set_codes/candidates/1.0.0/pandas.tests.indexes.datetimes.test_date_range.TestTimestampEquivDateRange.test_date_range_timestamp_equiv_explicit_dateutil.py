@td.skip_if_windows_python_3
def test_date_range_timestamp_equiv_explicit_dateutil(self):
    from pandas._libs.tslibs.timezones import dateutil_gettz as gettz
    rng = date_range('20090415', '20090519', tz=gettz('US/Eastern'))
    stamp = rng[0]
    ts = Timestamp('20090415', tz=gettz('US/Eastern'), freq='D')
    assert ts == stamp