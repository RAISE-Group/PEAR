@pytest.mark.parametrize('dtype', [int, 'int64', 'int32', 'int16', 'int8', 'uint64', 'uint32', 'uint16', 'uint8'])
def test_constructor_int_dtype_float(self, dtype):
    if is_unsigned_integer_dtype(dtype):
        index_type = UInt64Index
    else:
        index_type = Int64Index
    expected = index_type([0, 1, 2, 3])
    result = Index([0.0, 1.0, 2.0, 3.0], dtype=dtype)
    tm.assert_index_equal(result, expected)