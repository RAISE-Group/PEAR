def test_eq_with_str(self, dtype):
    assert dtype == dtype.name
    assert dtype != dtype.name + '-suffix'