def check_modulus(self, lhs, arith1, rhs):
    ex = f'lhs {arith1} rhs'
    result = pd.eval(ex, engine=self.engine, parser=self.parser)
    expected = lhs % rhs
    tm.assert_almost_equal(result, expected)
    expected = self.ne.evaluate(f'expected {arith1} rhs')
    if isinstance(result, (DataFrame, Series)):
        tm.assert_almost_equal(result.values, expected)
    else:
        tm.assert_almost_equal(result, expected.item())