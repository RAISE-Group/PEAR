def _test_moments_consistency_mock_mean(self, mean, mock_mean):
    for x, is_constant, no_nans in self.data:
        mean_x = mean(x)
        if mock_mean:
            expected = mock_mean(x)
            tm.assert_equal(mean_x, expected.astype('float64'))