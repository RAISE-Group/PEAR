def check_single_invert_op(self, lhs, cmp1, rhs):
    for el in (lhs, rhs):
        try:
            elb = el.astype(bool)
        except AttributeError:
            elb = np.array([bool(el)])
        expected = ~elb
        result = pd.eval('~elb', engine=self.engine, parser=self.parser)
        tm.assert_almost_equal(expected, result)
        for engine in self.current_engines:
            tm.assert_almost_equal(result, pd.eval('~elb', engine=engine, parser=self.parser))