def test_axis(self):
    samples = np.vstack([self.samples, np.nan * np.ones(len(self.samples))])
    kurt = nanops.nankurt(samples, axis=1)
    tm.assert_almost_equal(kurt, np.array([self.actual_kurt, np.nan]))