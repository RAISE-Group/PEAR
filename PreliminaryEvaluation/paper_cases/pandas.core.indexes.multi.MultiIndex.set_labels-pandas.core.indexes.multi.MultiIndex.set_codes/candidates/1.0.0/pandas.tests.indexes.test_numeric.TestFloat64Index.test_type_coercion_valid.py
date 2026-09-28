def test_type_coercion_valid(self, float_dtype):
    i = Index([1, 2, 3.5], dtype=float_dtype)
    tm.assert_index_equal(i, Index([1, 2, 3.5]))