def test_rank_desc_mix_nans_infs(self):
    iseries = Series([1, np.nan, np.inf, -np.inf, 25])
    result = iseries.rank(ascending=False)
    exp = Series([3, np.nan, 1, 4, 2], dtype='float64')
    tm.assert_series_equal(result, exp)