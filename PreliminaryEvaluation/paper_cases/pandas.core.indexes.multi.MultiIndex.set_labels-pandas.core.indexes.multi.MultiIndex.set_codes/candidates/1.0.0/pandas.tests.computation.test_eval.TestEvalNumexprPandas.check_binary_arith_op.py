def check_binary_arith_op(self, lhs, arith1, rhs):
    ex = f'lhs {arith1} rhs'
    result = pd.eval(ex, engine=self.engine, parser=self.parser)
    expected = _eval_single_bin(lhs, arith1, rhs, self.engine)
    tm.assert_almost_equal(result, expected)
    ex = f'lhs {arith1} rhs {arith1} rhs'
    result = pd.eval(ex, engine=self.engine, parser=self.parser)
    nlhs = _eval_single_bin(lhs, arith1, rhs, self.engine)
    self.check_alignment(result, nlhs, rhs, arith1)