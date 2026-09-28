def test_array_type_with_arg(self, data, dtype):
    assert dtype.construct_array_type() is SparseArray