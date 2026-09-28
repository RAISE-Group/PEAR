def test_eq_with_self(self, dtype):
    assert dtype == dtype
    assert dtype != object()