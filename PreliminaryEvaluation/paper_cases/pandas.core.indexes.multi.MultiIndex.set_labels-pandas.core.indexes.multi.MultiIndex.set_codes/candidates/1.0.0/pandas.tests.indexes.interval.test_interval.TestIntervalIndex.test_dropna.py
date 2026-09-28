def test_dropna(self, closed):
    expected = IntervalIndex.from_tuples([(0.0, 1.0), (1.0, 2.0)], closed=closed)
    ii = IntervalIndex.from_tuples([(0, 1), (1, 2), np.nan], closed=closed)
    result = ii.dropna()
    tm.assert_index_equal(result, expected)
    ii = IntervalIndex.from_arrays([0, 1, np.nan], [1, 2, np.nan], closed=closed)
    result = ii.dropna()
    tm.assert_index_equal(result, expected)