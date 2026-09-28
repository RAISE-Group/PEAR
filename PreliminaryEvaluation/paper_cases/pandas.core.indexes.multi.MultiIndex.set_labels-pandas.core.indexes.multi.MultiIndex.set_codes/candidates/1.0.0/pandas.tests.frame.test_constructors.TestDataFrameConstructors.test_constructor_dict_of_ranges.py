def test_constructor_dict_of_ranges(self):
    data = {'a': range(3), 'b': range(3, 6)}
    result = DataFrame(data)
    expected = DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]})
    tm.assert_frame_equal(result, expected)