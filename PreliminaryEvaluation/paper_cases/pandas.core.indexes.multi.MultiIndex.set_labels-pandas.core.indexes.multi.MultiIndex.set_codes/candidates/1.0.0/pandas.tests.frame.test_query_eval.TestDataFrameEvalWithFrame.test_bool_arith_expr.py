def test_bool_arith_expr(self, parser, engine):
    res = self.frame.eval('a[a < 1] + b', engine=engine, parser=parser)
    expect = self.frame.a[self.frame.a < 1] + self.frame.b
    tm.assert_series_equal(res, expect)