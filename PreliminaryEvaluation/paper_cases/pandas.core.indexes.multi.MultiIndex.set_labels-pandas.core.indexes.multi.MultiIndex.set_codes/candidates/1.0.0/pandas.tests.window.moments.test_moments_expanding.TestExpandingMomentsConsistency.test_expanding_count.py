def test_expanding_count(self):
    result = self.series.expanding(min_periods=0).count()
    tm.assert_almost_equal(result, self.series.rolling(window=len(self.series), min_periods=0).count())