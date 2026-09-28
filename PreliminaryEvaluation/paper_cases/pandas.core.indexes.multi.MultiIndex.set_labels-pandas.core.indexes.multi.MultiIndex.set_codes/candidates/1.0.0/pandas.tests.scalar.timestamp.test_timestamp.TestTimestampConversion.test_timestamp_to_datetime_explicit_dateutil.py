@td.skip_if_windows_python_3
def test_timestamp_to_datetime_explicit_dateutil(self):
    stamp = Timestamp('20090415', tz=gettz('US/Eastern'), freq='D')
    dtval = stamp.to_pydatetime()
    assert stamp == dtval
    assert stamp.tzinfo == dtval.tzinfo