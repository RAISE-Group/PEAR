def test_multi_line_expression_callable_local_variable_with_kwargs(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    def local_func(a, b):
        return b
    expected = df.copy()
    expected['c'] = expected['a'] * local_func(b=7, a=1)
    expected['d'] = expected['c'] + local_func(b=7, a=1)
    ans = df.eval('\n        c = a * @local_func(b=7, a=1)\n        d = c + @local_func(b=7, a=1)\n        ', inplace=True)
    tm.assert_frame_equal(expected, df)
    assert ans is None