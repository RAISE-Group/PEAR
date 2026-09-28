def test_large_series(self):
    s = Series(np.arange(1000000), index=IntervalIndex.from_breaks(np.arange(1000001)))
    result1 = s.loc[:80000]
    result2 = s.loc[0:80000]
    result3 = s.loc[0:80000:1]
    tm.assert_series_equal(result1, result2)
    tm.assert_series_equal(result1, result3)