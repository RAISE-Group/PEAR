def test_multi_line_expression_not_inplace(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    expected = df.copy()
    expected['c'] = expected['a'] + expected['b']
    expected['d'] = expected['c'] + expected['b']
    df = df.eval('\n        c = a + b\n        d = c + b', inplace=False)
    tm.assert_frame_equal(expected, df)
    expected['a'] = expected['a'] - 1
    expected['e'] = expected['a'] + 2
    df = df.eval('\n        a = a - 1\n        e = a + 2', inplace=False)
    tm.assert_frame_equal(expected, df)