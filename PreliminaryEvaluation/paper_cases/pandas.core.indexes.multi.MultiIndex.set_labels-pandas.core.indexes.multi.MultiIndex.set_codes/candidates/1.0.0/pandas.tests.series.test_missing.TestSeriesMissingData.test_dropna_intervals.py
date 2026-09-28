def test_dropna_intervals(self):
    s = Series([np.nan, 1, 2, 3], IntervalIndex.from_arrays([np.nan, 0, 1, 2], [np.nan, 1, 2, 3]))
    result = s.dropna()
    expected = s.iloc[1:]
    tm.assert_series_equal(result, expected)