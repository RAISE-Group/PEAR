def test_multi_line_expression(self):
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    expected = df.copy()
    expected['c'] = expected['a'] + expected['b']
    expected['d'] = expected['c'] + expected['b']
    ans = df.eval('\n        c = a + b\n        d = c + b', inplace=True)
    tm.assert_frame_equal(expected, df)
    assert ans is None
    expected['a'] = expected['a'] - 1
    expected['e'] = expected['a'] + 2
    ans = df.eval('\n        a = a - 1\n        e = a + 2', inplace=True)
    tm.assert_frame_equal(expected, df)
    assert ans is None
    with pytest.raises(ValueError):
        df.eval('\n            a = b + 2\n            b - 2', inplace=False)