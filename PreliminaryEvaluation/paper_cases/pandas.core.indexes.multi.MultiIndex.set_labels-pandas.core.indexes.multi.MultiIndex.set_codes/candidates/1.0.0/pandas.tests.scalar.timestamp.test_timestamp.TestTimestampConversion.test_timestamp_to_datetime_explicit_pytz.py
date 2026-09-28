def test_timestamp_to_datetime_explicit_pytz(self):
    stamp = Timestamp('20090415', tz=pytz.timezone('US/Eastern'), freq='D')
    dtval = stamp.to_pydatetime()
    assert stamp == dtval
    assert stamp.tzinfo == dtval.tzinfo