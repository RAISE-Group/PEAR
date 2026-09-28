def test_nested_scope(self):
    from pandas.core.computation.ops import UndefinedVariableError
    engine = self.engine
    parser = self.parser
    x = 1
    result = pd.eval('x + 1', engine=engine, parser=parser)
    assert result == 2
    df = DataFrame(np.random.randn(5, 3))
    df2 = DataFrame(np.random.randn(5, 3))
    with pytest.raises(SyntaxError):
        df.query('(@df>0) & (@df2>0)', engine=engine, parser=parser)
    with pytest.raises(UndefinedVariableError, match="name 'df' is not defined"):
        df.query('(df>0) & (df2>0)', engine=engine, parser=parser)
    expected = df[(df > 0) & (df2 > 0)]
    result = pd.eval('df[(df > 0) & (df2 > 0)]', engine=engine, parser=parser)
    tm.assert_frame_equal(expected, result)
    expected = df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]
    result = pd.eval('df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]', engine=engine, parser=parser)
    tm.assert_frame_equal(expected, result)