def test_series_negate(self):
    expr = self.ex('-')
    lhs = Series(randn(5))
    expect = -lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_series_equal(expect, result)
    lhs = Series(randint(5, size=5))
    expect = -lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_series_equal(expect, result)
    lhs = Series(rand(5) > 0.5)
    if self.engine == 'numexpr':
        with pytest.raises(NotImplementedError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)
    else:
        expect = -lhs
        result = pd.eval(expr, engine=self.engine, parser=self.parser)
        tm.assert_series_equal(expect, result)