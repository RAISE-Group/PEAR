def test_expanding_cov_pairwise(self):
    result = self.frame.expanding().corr()
    rolling_result = self.frame.rolling(window=len(self.frame), min_periods=1).corr()
    tm.assert_frame_equal(result, rolling_result)