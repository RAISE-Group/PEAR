@pytest.mark.parametrize('op', [operator.pow, ops.rpow])
def test_pow_float(self, op, numeric_idx, box_with_array):
    box = box_with_array
    idx = numeric_idx
    expected = pd.Float64Index(op(idx.values, 2.0))
    idx = tm.box_expected(idx, box)
    expected = tm.box_expected(expected, box)
    result = op(idx, 2.0)
    tm.assert_equal(result, expected)