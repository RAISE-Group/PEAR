def test_add(self, offset_types, tz_naive_fixture):
    tz = tz_naive_fixture
    dt = datetime(2011, 1, 1, 9, 0)
    offset_s = self._get_offset(offset_types)
    expected = self.expecteds[offset_types.__name__]
    result_dt = dt + offset_s
    result_ts = Timestamp(dt) + offset_s
    for result in [result_dt, result_ts]:
        assert isinstance(result, Timestamp)
        assert result == expected
    expected_localize = expected.tz_localize(tz)
    result = Timestamp(dt, tz=tz) + offset_s
    assert isinstance(result, Timestamp)
    assert result == expected_localize
    if issubclass(offset_types, Tick):
        return
    offset_s = self._get_offset(offset_types, normalize=True)
    expected = Timestamp(expected.date())
    result_dt = dt + offset_s
    result_ts = Timestamp(dt) + offset_s
    for result in [result_dt, result_ts]:
        assert isinstance(result, Timestamp)
        assert result == expected
    expected_localize = expected.tz_localize(tz)
    result = Timestamp(dt, tz=tz) + offset_s
    assert isinstance(result, Timestamp)
    assert result == expected_localize