def test_no_mode(self):
    exp = Series([], dtype=np.float64)
    tm.assert_series_equal(algos.mode([]), exp)