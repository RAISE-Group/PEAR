def test_div_zero(self, zero, numeric_idx):
    idx = numeric_idx
    expected = pd.Index([np.nan, np.inf, np.inf, np.inf, np.inf], dtype=np.float64)
    expected2 = adjust_negative_zero(zero, expected)
    result = idx / zero
    tm.assert_index_equal(result, expected2)
    ser_compat = Series(idx).astype('i8') / np.array(zero).astype('i8')
    tm.assert_series_equal(ser_compat, Series(expected))