def test_expanding_quantile(self):
    result = self.series.expanding().quantile(0.5)
    rolling_result = self.series.rolling(window=len(self.series), min_periods=1).quantile(0.5)
    tm.assert_almost_equal(result, rolling_result)