def test_inf(self):
    n = 10
    df = DataFrame({'a': np.random.rand(n), 'b': np.random.rand(n)})
    df.loc[::2, 0] = np.inf
    ops = ('==', '!=')
    d = dict(zip(ops, (operator.eq, operator.ne)))
    for op, f in d.items():
        q = 'a {op} inf'.format(op=op)
        expected = df[f(df.a, np.inf)]
        result = df.query(q, engine=self.engine, parser=self.parser)
        tm.assert_frame_equal(result, expected)