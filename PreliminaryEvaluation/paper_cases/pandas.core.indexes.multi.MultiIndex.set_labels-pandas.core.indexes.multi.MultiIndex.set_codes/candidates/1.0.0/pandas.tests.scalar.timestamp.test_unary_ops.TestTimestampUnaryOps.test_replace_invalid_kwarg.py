def test_replace_invalid_kwarg(self, tz_aware_fixture):
    tz = tz_aware_fixture
    ts = Timestamp('2016-01-01 09:00:00.000000123', tz=tz)
    with pytest.raises(TypeError):
        ts.replace(foo=5)