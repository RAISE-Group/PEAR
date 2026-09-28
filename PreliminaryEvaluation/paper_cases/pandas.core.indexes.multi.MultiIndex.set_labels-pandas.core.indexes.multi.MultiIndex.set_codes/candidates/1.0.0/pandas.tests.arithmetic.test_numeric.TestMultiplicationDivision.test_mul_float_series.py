def test_mul_float_series(self, numeric_idx):
    idx = numeric_idx
    rng5 = np.arange(5, dtype='float64')
    result = idx * Series(rng5 + 0.1)
    expected = Series(rng5 * (rng5 + 0.1))
    tm.assert_series_equal(result, expected)