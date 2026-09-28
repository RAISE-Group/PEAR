def test_hash_vs_equality(self):
    dtype = self.dtype
    dtype2 = DatetimeTZDtype('ns', 'US/Eastern')
    dtype3 = DatetimeTZDtype(dtype2)
    assert dtype == dtype2
    assert dtype2 == dtype
    assert dtype3 == dtype
    assert hash(dtype) == hash(dtype2)
    assert hash(dtype) == hash(dtype3)
    dtype4 = DatetimeTZDtype('ns', 'US/Central')
    assert dtype2 != dtype4
    assert hash(dtype2) != hash(dtype4)