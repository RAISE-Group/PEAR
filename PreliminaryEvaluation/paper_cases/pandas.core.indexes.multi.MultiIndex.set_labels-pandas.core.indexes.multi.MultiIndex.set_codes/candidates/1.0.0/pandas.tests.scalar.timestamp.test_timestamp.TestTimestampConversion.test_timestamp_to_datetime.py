def test_timestamp_to_datetime(self):
    stamp = Timestamp('20090415', tz='US/Eastern', freq='D')
    dtval = stamp.to_pydatetime()
    assert stamp == dtval
    assert stamp.tzinfo == dtval.tzinfo