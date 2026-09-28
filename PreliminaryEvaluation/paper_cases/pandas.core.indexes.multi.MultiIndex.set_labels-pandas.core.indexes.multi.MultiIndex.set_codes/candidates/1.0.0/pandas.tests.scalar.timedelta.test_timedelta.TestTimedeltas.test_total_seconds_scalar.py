def test_total_seconds_scalar(self):
    rng = Timedelta('1 days, 10:11:12.100123456')
    expt = 1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1000000000.0
    tm.assert_almost_equal(rng.total_seconds(), expt)
    rng = Timedelta(np.nan)
    assert np.isnan(rng.total_seconds())