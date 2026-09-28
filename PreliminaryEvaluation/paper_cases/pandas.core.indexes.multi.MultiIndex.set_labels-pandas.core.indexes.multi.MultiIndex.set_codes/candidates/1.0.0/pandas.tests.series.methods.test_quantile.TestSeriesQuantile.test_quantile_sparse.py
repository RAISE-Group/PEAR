@pytest.mark.parametrize('values, dtype', [([0, 0, 0, 1, 2, 3], 'Sparse[int]'), ([0.0, None, 1.0, 2.0], 'Sparse[float]')])
def test_quantile_sparse(self, values, dtype):
    ser = pd.Series(values, dtype=dtype)
    result = ser.quantile([0.5])
    expected = pd.Series(np.asarray(ser)).quantile([0.5])
    tm.assert_series_equal(result, expected)