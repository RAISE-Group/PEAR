def test_nans_skipna(self):
    samples = np.hstack([self.samples, np.nan])
    skew = nanops.nanskew(samples, skipna=True)
    tm.assert_almost_equal(skew, self.actual_skew)