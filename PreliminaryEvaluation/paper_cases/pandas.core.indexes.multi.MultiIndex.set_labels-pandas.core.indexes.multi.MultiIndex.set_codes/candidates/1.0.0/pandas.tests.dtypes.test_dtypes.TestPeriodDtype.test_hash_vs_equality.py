def test_hash_vs_equality(self):
    dtype = self.dtype
    dtype2 = PeriodDtype('D')
    dtype3 = PeriodDtype(dtype2)
    assert dtype == dtype2
    assert dtype2 == dtype
    assert dtype3 == dtype
    assert dtype is dtype2
    assert dtype2 is dtype
    assert dtype3 is dtype
    assert hash(dtype) == hash(dtype2)
    assert hash(dtype) == hash(dtype3)