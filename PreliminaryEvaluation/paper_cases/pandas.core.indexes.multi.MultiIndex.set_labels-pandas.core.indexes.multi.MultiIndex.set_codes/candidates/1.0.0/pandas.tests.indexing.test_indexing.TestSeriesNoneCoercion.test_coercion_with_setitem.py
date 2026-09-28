def test_coercion_with_setitem(self):
    for start_data, expected_result in self.EXPECTED_RESULTS:
        start_series = Series(start_data)
        start_series[0] = None
        expected_series = Series(expected_result)
        tm.assert_series_equal(start_series, expected_series)