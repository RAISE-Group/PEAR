def test_frame_negate(self):
    expr = self.ex('-')
    lhs = DataFrame(randn(5, 2))
    expect = -lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_frame_equal(expect, result)
    lhs = DataFrame(randint(5, size=(5, 2)))
    expect = -lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_frame_equal(expect, result)
    lhs = DataFrame(rand(5, 2) > 0.5)
    if self.engine == 'numexpr':
        with pytest.raises(NotImplementedError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)
    else:
        expect = -lhs
        result = pd.eval(expr, engine=self.engine, parser=self.parser)
        tm.assert_frame_equal(expect, result)