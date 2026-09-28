def test_frame_pos(self):
    expr = self.ex('+')
    lhs = DataFrame(randn(5, 2))
    expect = lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_frame_equal(expect, result)
    lhs = DataFrame(randint(5, size=(5, 2)))
    expect = lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_frame_equal(expect, result)
    lhs = DataFrame(rand(5, 2) > 0.5)
    expect = lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_frame_equal(expect, result)