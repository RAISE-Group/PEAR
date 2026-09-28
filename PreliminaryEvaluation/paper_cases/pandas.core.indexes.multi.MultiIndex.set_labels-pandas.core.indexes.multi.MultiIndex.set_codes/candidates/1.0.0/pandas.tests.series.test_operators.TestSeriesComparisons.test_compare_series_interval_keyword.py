def test_compare_series_interval_keyword(self):
    s = Series(['IntervalA', 'IntervalB', 'IntervalC'])
    result = s == 'IntervalA'
    expected = Series([True, False, False])
    tm.assert_series_equal(result, expected)