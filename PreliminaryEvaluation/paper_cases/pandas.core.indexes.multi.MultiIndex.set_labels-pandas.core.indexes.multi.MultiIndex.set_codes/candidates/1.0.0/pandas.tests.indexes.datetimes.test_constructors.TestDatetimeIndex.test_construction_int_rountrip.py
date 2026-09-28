def test_construction_int_rountrip(self, tz_naive_fixture):
    tz = tz_naive_fixture
    result = 1293858000000000000
    expected = DatetimeIndex([result], tz=tz).asi8[0]
    assert result == expected