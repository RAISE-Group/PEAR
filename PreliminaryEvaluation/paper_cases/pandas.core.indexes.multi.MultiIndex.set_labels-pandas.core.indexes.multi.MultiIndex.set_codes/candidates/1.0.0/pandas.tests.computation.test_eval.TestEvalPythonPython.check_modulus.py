def check_modulus(self, lhs, arith1, rhs):
    ex = f'lhs {arith1} rhs'
    result = pd.eval(ex, engine=self.engine, parser=self.parser)
    expected = lhs % rhs
    tm.assert_almost_equal(result, expected)
    expected = _eval_single_bin(expected, arith1, rhs, self.engine)
    tm.assert_almost_equal(result, expected)