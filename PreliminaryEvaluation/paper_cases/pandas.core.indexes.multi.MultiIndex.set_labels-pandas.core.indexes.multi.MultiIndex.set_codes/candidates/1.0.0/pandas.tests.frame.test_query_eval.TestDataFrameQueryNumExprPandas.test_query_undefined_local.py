def test_query_undefined_local(self):
    from pandas.core.computation.ops import UndefinedVariableError
    engine, parser = (self.engine, self.parser)
    skip_if_no_pandas_parser(parser)
    df = DataFrame(np.random.rand(10, 2), columns=list('ab'))
    with pytest.raises(UndefinedVariableError, match="local variable 'c' is not defined"):
        df.query('a == @c', engine=engine, parser=parser)