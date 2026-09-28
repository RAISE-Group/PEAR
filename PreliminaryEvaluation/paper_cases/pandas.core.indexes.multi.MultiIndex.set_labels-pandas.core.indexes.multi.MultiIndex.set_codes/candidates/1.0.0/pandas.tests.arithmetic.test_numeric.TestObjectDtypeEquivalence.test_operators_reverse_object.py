@pytest.mark.parametrize('op', [operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv])
def test_operators_reverse_object(self, op):
    arr = pd.Series(np.random.randn(10), index=np.arange(10), dtype=object)
    result = op(1.0, arr)
    expected = op(1.0, arr.astype(float))
    tm.assert_series_equal(result.astype(float), expected)