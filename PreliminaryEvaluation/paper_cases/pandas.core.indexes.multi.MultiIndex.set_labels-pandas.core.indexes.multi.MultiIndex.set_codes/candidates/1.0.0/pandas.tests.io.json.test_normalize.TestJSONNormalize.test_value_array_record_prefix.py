def test_value_array_record_prefix(self):
    result = json_normalize({'A': [1, 2]}, 'A', record_prefix='Prefix.')
    expected = DataFrame([[1], [2]], columns=['Prefix.0'])
    tm.assert_frame_equal(result, expected)