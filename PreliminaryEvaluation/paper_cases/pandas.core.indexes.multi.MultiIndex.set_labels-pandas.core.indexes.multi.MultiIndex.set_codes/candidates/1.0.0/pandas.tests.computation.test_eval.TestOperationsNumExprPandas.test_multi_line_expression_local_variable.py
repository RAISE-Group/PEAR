def test_multi_line_expression_local_variable(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    expected = df.copy()
    local_var = 7
    expected['c'] = expected['a'] * local_var
    expected['d'] = expected['c'] + local_var
    ans = df.eval('\n        c = a * @local_var\n        d = c + @local_var\n        ', inplace=True)
    tm.assert_frame_equal(expected, df)
    assert ans is None