def test_axis(self):
    samples = np.vstack([self.samples, np.nan * np.ones(len(self.samples))])
    skew = nanops.nanskew(samples, axis=1)
    tm.assert_almost_equal(skew, np.array([self.actual_skew, np.nan]))