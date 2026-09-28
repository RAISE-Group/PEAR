def test_assignment_column(self):
    df = DataFrame(np.random.randn(5, 2), columns=list('ab'))
    orig_df = df.copy()
    with pytest.raises(SyntaxError, match='invalid syntax'):
        df.eval('d c = a + b')
    msg = 'left hand side of an assignment must be a single name'
    with pytest.raises(SyntaxError, match=msg):
        df.eval('d,c = a + b')
    if compat.PY38:
        msg = 'cannot assign to function call'
    else:
        msg = "can't assign to function call"
    with pytest.raises(SyntaxError, match=msg):
        df.eval('Timestamp("20131001") = a + b')
    expected = orig_df.copy()
    expected['a'] = expected['a'] + expected['b']
    df = orig_df.copy()
    df.eval('a = a + b', inplace=True)
    tm.assert_frame_equal(df, expected)
    expected = orig_df.copy()
    expected['c'] = expected['a'] + expected['b']
    df = orig_df.copy()
    df.eval('c = a + b', inplace=True)
    tm.assert_frame_equal(df, expected)

    def f():
        df = orig_df.copy()
        a = 1
        df.eval('a = 1 + b', inplace=True)
        return df
    df = f()
    expected = orig_df.copy()
    expected['a'] = 1 + expected['b']
    tm.assert_frame_equal(df, expected)
    df = orig_df.copy()

    def f():
        a = 1
        old_a = df.a.copy()
        df.eval('a = a + b', inplace=True)
        result = old_a + df.b
        tm.assert_series_equal(result, df.a, check_names=False)
        assert result.name is None
    f()
    df = orig_df.copy()
    df.eval('c = a + b', inplace=True)
    msg = 'can only assign a single expression'
    with pytest.raises(SyntaxError, match=msg):
        df.eval('c = a = b')
    df = orig_df.copy()
    self.eval('c = df.a + df.b', local_dict={'df': df}, target=df, inplace=True)
    expected = orig_df.copy()
    expected['c'] = expected['a'] + expected['b']
    tm.assert_frame_equal(df, expected)