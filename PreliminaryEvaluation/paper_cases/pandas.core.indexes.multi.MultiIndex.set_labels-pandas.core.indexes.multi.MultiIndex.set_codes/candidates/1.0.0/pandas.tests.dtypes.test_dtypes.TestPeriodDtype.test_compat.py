def test_compat(self):
    assert not is_datetime64_ns_dtype(self.dtype)
    assert not is_datetime64_ns_dtype('period[D]')
    assert not is_datetime64_dtype(self.dtype)
    assert not is_datetime64_dtype('period[D]')