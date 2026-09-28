def test_pickle_strings(self, string_series):
    unp_series = self._pickle_roundtrip(string_series)
    tm.assert_series_equal(unp_series, string_series)