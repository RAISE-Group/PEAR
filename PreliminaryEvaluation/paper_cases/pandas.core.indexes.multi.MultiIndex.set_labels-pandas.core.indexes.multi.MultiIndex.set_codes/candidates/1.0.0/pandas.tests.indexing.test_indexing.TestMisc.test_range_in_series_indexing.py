def test_range_in_series_indexing(self):
    for x in [5, 999999, 1000000]:
        s = Series(index=range(x), dtype=np.float64)
        s.loc[range(1)] = 42
        tm.assert_series_equal(s.loc[range(1)], Series(42.0, index=[0]))
        s.loc[range(2)] = 43
        tm.assert_series_equal(s.loc[range(2)], Series(43.0, index=[0, 1]))