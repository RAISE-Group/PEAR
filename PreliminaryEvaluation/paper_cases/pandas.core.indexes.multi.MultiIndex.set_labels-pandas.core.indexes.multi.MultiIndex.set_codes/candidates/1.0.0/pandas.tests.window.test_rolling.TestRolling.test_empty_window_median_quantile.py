def test_empty_window_median_quantile(self):
    expected = pd.Series([np.nan, np.nan, np.nan])
    roll = pd.Series(np.arange(3)).rolling(0)
    result = roll.median()
    tm.assert_series_equal(result, expected)
    result = roll.quantile(0.1)
    tm.assert_series_equal(result, expected)