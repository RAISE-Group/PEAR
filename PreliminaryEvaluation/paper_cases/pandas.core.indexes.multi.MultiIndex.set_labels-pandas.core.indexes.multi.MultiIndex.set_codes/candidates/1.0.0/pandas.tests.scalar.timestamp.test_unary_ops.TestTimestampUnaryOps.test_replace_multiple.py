def test_replace_multiple(self, tz_aware_fixture):
    tz = tz_aware_fixture
    ts = Timestamp('2016-01-01 09:00:00.000000123', tz=tz)
    result = ts.replace(year=2015, month=2, day=2, hour=0, minute=5, second=5, microsecond=5, nanosecond=5)
    expected = Timestamp('2015-02-02 00:05:05.000005005', tz=tz)
    assert result == expected