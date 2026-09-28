def test_multi_line_expression_callable_local_variable(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    def local_func(a, b):
        return b
    expected = df.copy()
    expected['c'] = expected['a'] * local_func(1, 7)
    expected['d'] = expected['c'] + local_func(1, 7)
    ans = df.eval('\n        c = a * @local_func(1, 7)\n        d = c + @local_func(1, 7)\n        ', inplace=True)
    tm.assert_frame_equal(expected, df)
    assert ans is None