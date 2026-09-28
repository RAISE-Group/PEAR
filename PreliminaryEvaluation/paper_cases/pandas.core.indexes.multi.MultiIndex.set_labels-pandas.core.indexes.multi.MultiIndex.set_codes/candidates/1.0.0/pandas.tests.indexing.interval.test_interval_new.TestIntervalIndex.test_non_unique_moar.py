def test_non_unique_moar(self):
    idx = IntervalIndex.from_tuples([(1, 3), (1, 3), (3, 7)])
    s = Series(range(len(idx)), index=idx)
    expected = s.iloc[[0, 1]]
    result = s.loc[Interval(1, 3)]
    tm.assert_series_equal(expected, result)
    expected = s
    result = s.loc[Interval(1, 3):]
    tm.assert_series_equal(expected, result)
    expected = s
    result = s[Interval(1, 3):]
    tm.assert_series_equal(expected, result)
    expected = s.iloc[[0, 1]]
    result = s[[Interval(1, 3)]]
    tm.assert_series_equal(expected, result)