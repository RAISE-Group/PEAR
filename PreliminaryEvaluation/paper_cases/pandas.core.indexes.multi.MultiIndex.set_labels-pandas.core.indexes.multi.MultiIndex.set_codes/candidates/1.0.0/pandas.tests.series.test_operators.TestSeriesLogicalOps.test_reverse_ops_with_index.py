@pytest.mark.parametrize('op, expected', [(ops.rand_, pd.Index([False, True])), (ops.ror_, pd.Index([False, True])), (ops.rxor, pd.Index([]))])
def test_reverse_ops_with_index(self, op, expected):
    ser = Series([True, False])
    idx = Index([False, True])
    result = op(ser, idx)
    tm.assert_index_equal(result, expected)