def test_check_many_exprs(self):
    a = 1
    expr = ' * '.join('a' * 33)
    expected = 1
    res = pd.eval(expr, engine=self.engine, parser=self.parser)
    assert res == expected