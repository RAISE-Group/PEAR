def test_value_counts_bins(self):
    s = [1, 2, 3, 4]
    result = algos.value_counts(s, bins=1)
    expected = Series([4], index=IntervalIndex.from_tuples([(0.996, 4.0)]))
    tm.assert_series_equal(result, expected)
    result = algos.value_counts(s, bins=2, sort=False)
    expected = Series([2, 2], index=IntervalIndex.from_tuples([(0.996, 2.5), (2.5, 4.0)]))
    tm.assert_series_equal(result, expected)