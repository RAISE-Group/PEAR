@td.skip_if_windows
def test_timestamp(self):
    ts = Timestamp.now()
    uts = ts.replace(tzinfo=utc)
    assert ts.timestamp() == uts.timestamp()
    tsc = Timestamp('2014-10-11 11:00:01.12345678', tz='US/Central')
    utsc = tsc.tz_convert('UTC')
    assert tsc.timestamp() == utsc.timestamp()
    with tm.set_timezone('UTC'):
        dt = ts.to_pydatetime()
        assert dt.timestamp() == ts.timestamp()