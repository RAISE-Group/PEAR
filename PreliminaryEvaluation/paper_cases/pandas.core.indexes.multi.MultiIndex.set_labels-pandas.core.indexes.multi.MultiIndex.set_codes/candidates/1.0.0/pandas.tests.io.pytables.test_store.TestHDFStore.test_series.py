def test_series(self, setup_path):
    s = tm.makeStringSeries()
    self._check_roundtrip(s, tm.assert_series_equal, path=setup_path)
    ts = tm.makeTimeSeries()
    self._check_roundtrip(ts, tm.assert_series_equal, path=setup_path)
    ts2 = Series(ts.index, Index(ts.index, dtype=object))
    self._check_roundtrip(ts2, tm.assert_series_equal, path=setup_path)
    ts3 = Series(ts.values, Index(np.asarray(ts.index, dtype=object), dtype=object))
    self._check_roundtrip(ts3, tm.assert_series_equal, path=setup_path, check_index_type=False)