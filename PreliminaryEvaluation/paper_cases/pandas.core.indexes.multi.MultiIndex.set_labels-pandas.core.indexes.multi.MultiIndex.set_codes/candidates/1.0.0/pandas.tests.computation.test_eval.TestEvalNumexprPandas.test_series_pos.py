def test_series_pos(self):
    expr = self.ex('+')
    lhs = Series(randn(5))
    expect = lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_series_equal(expect, result)
    lhs = Series(randint(5, size=5))
    expect = lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_series_equal(expect, result)
    lhs = Series(rand(5) > 0.5)
    expect = lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_series_equal(expect, result)