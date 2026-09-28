def test_replace_integer_args(self, tz_aware_fixture):
    tz = tz_aware_fixture
    ts = Timestamp('2016-01-01 09:00:00.000000123', tz=tz)
    with pytest.raises(ValueError):
        ts.replace(hour=0.1)