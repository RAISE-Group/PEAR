def test_query_scope(self):
    from pandas.core.computation.ops import UndefinedVariableError
    engine, parser = (self.engine, self.parser)
    skip_if_no_pandas_parser(parser)
    df = DataFrame(np.random.randn(20, 2), columns=list('ab'))
    a, b = (1, 2)
    res = df.query('a > b', engine=engine, parser=parser)
    expected = df[df.a > df.b]
    tm.assert_frame_equal(res, expected)
    res = df.query('@a > b', engine=engine, parser=parser)
    expected = df[a > df.b]
    tm.assert_frame_equal(res, expected)
    with pytest.raises(UndefinedVariableError, match="local variable 'c' is not defined"):
        df.query('@a > b > @c', engine=engine, parser=parser)
    with pytest.raises(UndefinedVariableError, match="name 'c' is not defined"):
        df.query('@a > b > c', engine=engine, parser=parser)