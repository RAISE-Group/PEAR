def test_arith_series_with_scalar(self, data, all_arithmetic_operators):
    op_name = all_arithmetic_operators
    if op_name != '__rmod__':
        super().test_arith_series_with_scalar(data, op_name)
    else:
        pytest.skip('rmod never called when string is first argument')