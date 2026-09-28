def test_values(self, datetime_series):
    tm.assert_almost_equal(datetime_series.values, datetime_series, check_dtype=False)