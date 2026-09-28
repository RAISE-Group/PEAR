def get_expected_pow_result(self, lhs, rhs):
    try:
        expected = _eval_single_bin(lhs, '**', rhs, self.engine)
    except ValueError as e:
        if str(e).startswith('negative number cannot be raised to a fractional power'):
            if self.engine == 'python':
                pytest.skip(str(e))
            else:
                expected = np.nan
        else:
            raise
    return expected