def test_frame_invert(self):
    expr = self.ex('~')
    lhs = DataFrame(randn(5, 2))
    if self.engine == 'numexpr':
        with pytest.raises(NotImplementedError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)
    else:
        with pytest.raises(TypeError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)
    lhs = DataFrame(randint(5, size=(5, 2)))
    if self.engine == 'numexpr':
        with pytest.raises(NotImplementedError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)
    else:
        expect = ~lhs
        result = pd.eval(expr, engine=self.engine, parser=self.parser)
        tm.assert_frame_equal(expect, result)
    lhs = DataFrame(rand(5, 2) > 0.5)
    expect = ~lhs
    result = pd.eval(expr, engine=self.engine, parser=self.parser)
    tm.assert_frame_equal(expect, result)
    lhs = DataFrame({'b': ['a', 1, 2.0], 'c': rand(3) > 0.5})
    if self.engine == 'numexpr':
        with pytest.raises(ValueError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)
    else:
        with pytest.raises(TypeError):
            result = pd.eval(expr, engine=self.engine, parser=self.parser)