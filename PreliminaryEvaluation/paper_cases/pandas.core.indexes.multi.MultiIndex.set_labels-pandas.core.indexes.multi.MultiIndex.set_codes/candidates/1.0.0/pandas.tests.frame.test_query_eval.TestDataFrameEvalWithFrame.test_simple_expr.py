def test_simple_expr(self, parser, engine):
    res = self.frame.eval('a + b', engine=engine, parser=parser)
    expect = self.frame.a + self.frame.b
    tm.assert_series_equal(res, expect)