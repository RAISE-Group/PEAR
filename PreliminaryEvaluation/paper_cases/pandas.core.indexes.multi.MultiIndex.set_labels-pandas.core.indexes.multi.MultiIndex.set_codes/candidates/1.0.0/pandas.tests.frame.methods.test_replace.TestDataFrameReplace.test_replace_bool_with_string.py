def test_replace_bool_with_string(self):
    df = DataFrame({'a': [True, False], 'b': list('ab')})
    result = df.replace(True, 'a')
    expected = DataFrame({'a': ['a', False], 'b': df.b})
    tm.assert_frame_equal(result, expected)