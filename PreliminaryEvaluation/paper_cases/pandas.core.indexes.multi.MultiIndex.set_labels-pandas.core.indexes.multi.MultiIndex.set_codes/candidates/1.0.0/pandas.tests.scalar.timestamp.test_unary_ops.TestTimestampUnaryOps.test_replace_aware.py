def test_replace_aware(self, tz_aware_fixture):
    tz = tz_aware_fixture
    ts = Timestamp('2016-01-01 09:00:00', tz=tz)
    result = ts.replace(hour=0)
    expected = Timestamp('2016-01-01 00:00:00', tz=tz)
    assert result == expected