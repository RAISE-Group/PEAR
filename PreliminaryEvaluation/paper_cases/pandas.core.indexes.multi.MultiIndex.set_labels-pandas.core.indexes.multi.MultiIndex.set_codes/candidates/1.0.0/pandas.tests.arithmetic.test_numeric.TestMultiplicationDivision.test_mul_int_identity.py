@pytest.mark.parametrize('op', [operator.mul, ops.rmul, operator.floordiv])
def test_mul_int_identity(self, op, numeric_idx, box_with_array):
    idx = numeric_idx
    idx = tm.box_expected(idx, box_with_array)
    result = op(idx, 1)
    tm.assert_equal(result, idx)