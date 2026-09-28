def test_nans_skipna(self):
    samples = np.hstack([self.samples, np.nan])
    kurt = nanops.nankurt(samples, skipna=True)
    tm.assert_almost_equal(kurt, self.actual_kurt)