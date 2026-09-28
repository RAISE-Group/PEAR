@pytest.mark.parametrize('dtype', [None, 'uint8', 'category'])
def test_constructor_range_dtype(self, dtype):
    expected = DataFrame({'A': [0, 1, 2, 3, 4]}, dtype=dtype or 'int64')
    result = DataFrame(range(5), columns=['A'], dtype=dtype)
    tm.assert_frame_equal(result, expected)
    result = DataFrame({'A': range(5)}, dtype=dtype)
    tm.assert_frame_equal(result, expected)