def test_missing_minp_zero(self):
    x = pd.Series([np.nan])
    result = x.expanding(min_periods=0).sum()
    expected = pd.Series([0.0])
    tm.assert_series_equal(result, expected)
    result = x.expanding(min_periods=1).sum()
    expected = pd.Series([np.nan])
    tm.assert_series_equal(result, expected)