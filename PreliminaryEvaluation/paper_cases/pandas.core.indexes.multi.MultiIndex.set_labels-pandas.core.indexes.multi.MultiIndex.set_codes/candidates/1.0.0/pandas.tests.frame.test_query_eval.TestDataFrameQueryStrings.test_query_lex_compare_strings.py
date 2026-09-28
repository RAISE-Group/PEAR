def test_query_lex_compare_strings(self, parser, engine):
    a = Series(np.random.choice(list('abcde'), 20))
    b = Series(np.arange(a.size))
    df = DataFrame({'X': a, 'Y': b})
    ops = {'<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge}
    for op, func in ops.items():
        res = df.query(f'X {op} "d"', engine=engine, parser=parser)
        expected = df[func(df.X, 'd')]
        tm.assert_frame_equal(res, expected)