def test_comparison_protected_from_errstate(self):
    missing_df = tm.makeDataFrame()
    missing_df.iloc[0]['A'] = np.nan
    with np.errstate(invalid='ignore'):
        expected = missing_df.values < 0
    with np.errstate(invalid='raise'):
        result = (missing_df < 0).values
    tm.assert_numpy_array_equal(result, expected)