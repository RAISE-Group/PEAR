def test_pickle_datetimes(self, datetime_series):
    unp_ts = self._pickle_roundtrip(datetime_series)
    tm.assert_series_equal(unp_ts, datetime_series)