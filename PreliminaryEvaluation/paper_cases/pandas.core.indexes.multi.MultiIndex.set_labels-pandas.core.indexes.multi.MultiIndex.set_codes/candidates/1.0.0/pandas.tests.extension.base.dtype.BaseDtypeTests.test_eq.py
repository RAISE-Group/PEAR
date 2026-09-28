def test_eq(self, dtype):
    assert dtype == dtype.name
    assert dtype != 'anonther_type'