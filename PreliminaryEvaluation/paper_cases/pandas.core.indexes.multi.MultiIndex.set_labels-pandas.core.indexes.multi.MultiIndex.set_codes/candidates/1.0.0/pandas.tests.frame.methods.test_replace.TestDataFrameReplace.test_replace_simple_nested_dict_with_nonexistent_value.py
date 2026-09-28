def test_replace_simple_nested_dict_with_nonexistent_value(self):
    df = DataFrame({'col': range(1, 5)})
    expected = DataFrame({'col': ['a', 2, 3, 'b']})
    result = df.replace({-1: '-', 1: 'a', 4: 'b'})
    tm.assert_frame_equal(expected, result)
    result = df.replace({'col': {-1: '-', 1: 'a', 4: 'b'}})
    tm.assert_frame_equal(expected, result)