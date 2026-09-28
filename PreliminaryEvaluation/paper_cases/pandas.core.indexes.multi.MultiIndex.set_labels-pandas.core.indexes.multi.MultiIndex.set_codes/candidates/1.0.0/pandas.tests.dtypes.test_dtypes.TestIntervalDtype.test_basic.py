def test_basic(self):
    assert is_interval_dtype(self.dtype)
    ii = IntervalIndex.from_breaks(range(3))
    assert is_interval_dtype(ii.dtype)
    assert is_interval_dtype(ii)
    s = Series(ii, name='A')
    assert is_interval_dtype(s.dtype)
    assert is_interval_dtype(s)