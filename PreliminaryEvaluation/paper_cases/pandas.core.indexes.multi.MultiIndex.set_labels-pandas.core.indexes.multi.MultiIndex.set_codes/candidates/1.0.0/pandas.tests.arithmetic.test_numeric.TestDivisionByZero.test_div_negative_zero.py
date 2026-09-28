@pytest.mark.parametrize('op', [operator.truediv, operator.floordiv])
def test_div_negative_zero(self, zero, numeric_idx, op):
    if isinstance(numeric_idx, pd.UInt64Index):
        return
    idx = numeric_idx - 3
    expected = pd.Index([-np.inf, -np.inf, -np.inf, np.nan, np.inf], dtype=np.float64)
    expected = adjust_negative_zero(zero, expected)
    result = op(idx, zero)
    tm.assert_index_equal(result, expected)