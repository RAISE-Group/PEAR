def test_hash_vs_equality(self):
    dtype = self.dtype
    dtype2 = CategoricalDtype()
    assert dtype == dtype2
    assert dtype2 == dtype
    assert hash(dtype) == hash(dtype2)