def test_contains(self, datetime_series):
    tm.assert_contains_all(datetime_series.index, datetime_series)