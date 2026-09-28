def test_nans(self):
    samples = np.hstack([self.samples, np.nan])
    skew = nanops.nanskew(samples, skipna=False)
    assert np.isnan(skew)