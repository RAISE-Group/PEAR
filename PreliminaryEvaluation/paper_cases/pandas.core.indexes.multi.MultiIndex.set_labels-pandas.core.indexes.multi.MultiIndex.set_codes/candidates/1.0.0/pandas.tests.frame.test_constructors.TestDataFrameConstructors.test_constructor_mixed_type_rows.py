def test_constructor_mixed_type_rows(self):
    data = [[1, 2], (3, 4)]
    result = DataFrame(data)
    expected = DataFrame([[1, 2], [3, 4]])
    tm.assert_frame_equal(result, expected)