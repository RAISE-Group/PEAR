def test_constructor_dtype_str(self):
    result = SparseArray([1, 2, 3], dtype='int')
    expected = SparseArray([1, 2, 3], dtype=int)
    tm.assert_sp_array_equal(result, expected)