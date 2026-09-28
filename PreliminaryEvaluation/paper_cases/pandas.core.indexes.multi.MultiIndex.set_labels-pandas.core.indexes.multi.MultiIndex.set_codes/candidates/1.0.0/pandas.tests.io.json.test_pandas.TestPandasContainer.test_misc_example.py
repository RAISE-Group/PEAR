def test_misc_example(self):
    result = read_json('[{"a": 1, "b": 2}, {"b":2, "a" :1}]', numpy=True)
    expected = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    error_msg = "DataFrame\\.index are different\n\nDataFrame\\.index values are different \\(100\\.0 %\\)\n\\[left\\]:  Index\\(\\['a', 'b'\\], dtype='object'\\)\n\\[right\\]: RangeIndex\\(start=0, stop=2, step=1\\)"
    with pytest.raises(AssertionError, match=error_msg):
        tm.assert_frame_equal(result, expected, check_index_type=False)
    result = read_json('[{"a": 1, "b": 2}, {"b":2, "a" :1}]')
    expected = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    tm.assert_frame_equal(result, expected)