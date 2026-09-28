def test_compat(self):
    assert is_datetime64tz_dtype(self.dtype)
    assert is_datetime64tz_dtype('datetime64[ns, US/Eastern]')
    assert is_datetime64_any_dtype(self.dtype)
    assert is_datetime64_any_dtype('datetime64[ns, US/Eastern]')
    assert is_datetime64_ns_dtype(self.dtype)
    assert is_datetime64_ns_dtype('datetime64[ns, US/Eastern]')
    assert not is_datetime64_dtype(self.dtype)
    assert not is_datetime64_dtype('datetime64[ns, US/Eastern]')