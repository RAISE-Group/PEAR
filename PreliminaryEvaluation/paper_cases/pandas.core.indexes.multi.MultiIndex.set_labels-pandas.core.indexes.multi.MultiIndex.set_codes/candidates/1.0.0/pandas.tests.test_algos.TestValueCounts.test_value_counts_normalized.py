def test_value_counts_normalized(self):
    s = Series([1, 2, np.nan, np.nan, np.nan])
    dtypes = (np.float64, np.object, 'M8[ns]')
    for t in dtypes:
        s_typed = s.astype(t)
        result = s_typed.value_counts(normalize=True, dropna=False)
        expected = Series([0.6, 0.2, 0.2], index=Series([np.nan, 2.0, 1.0], dtype=t))
        tm.assert_series_equal(result, expected)
        result = s_typed.value_counts(normalize=True, dropna=True)
        expected = Series([0.5, 0.5], index=Series([2.0, 1.0], dtype=t))
        tm.assert_series_equal(result, expected)