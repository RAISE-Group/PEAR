def test_delta_preserve_nanos(self):
    val = Timestamp(1337299200000000123)
    result = val + timedelta(1)
    assert result.nanosecond == val.nanosecond