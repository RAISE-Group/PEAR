def test_nans(self):
    samples = np.hstack([self.samples, np.nan])
    kurt = nanops.nankurt(samples, skipna=False)
    assert np.isnan(kurt)