def test_rsub_dtscalars(self, tz_naive_fixture):
    td = Timedelta(1235345642000)
    ts = Timestamp.now(tz_naive_fixture)
    other = ts + td
    assert other - ts == td
    assert other.to_pydatetime() - ts == td
    if tz_naive_fixture is None:
        assert other.to_datetime64() - ts == td
    else:
        with pytest.raises(TypeError, match='subtraction must have'):
            other.to_datetime64() - ts