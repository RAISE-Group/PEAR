def check_pow(self, lhs, arith1, rhs):
    ex = f'lhs {arith1} rhs'
    expected = self.get_expected_pow_result(lhs, rhs)
    result = pd.eval(ex, engine=self.engine, parser=self.parser)
    if is_scalar(lhs) and is_scalar(rhs) and _is_py3_complex_incompat(result, expected):
        with pytest.raises(AssertionError):
            tm.assert_numpy_array_equal(result, expected)
    else:
        tm.assert_almost_equal(result, expected)
        ex = f'(lhs {arith1} rhs) {arith1} rhs'
        result = pd.eval(ex, engine=self.engine, parser=self.parser)
        expected = self.get_expected_pow_result(self.get_expected_pow_result(lhs, rhs), rhs)
        tm.assert_almost_equal(result, expected)