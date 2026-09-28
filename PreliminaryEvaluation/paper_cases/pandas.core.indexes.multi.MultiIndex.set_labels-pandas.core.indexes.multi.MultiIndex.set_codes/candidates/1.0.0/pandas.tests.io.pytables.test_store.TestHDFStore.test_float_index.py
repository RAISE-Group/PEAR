def test_float_index(self, setup_path):
    index = np.random.randn(10)
    s = Series(np.random.randn(10), index=index)
    self._check_roundtrip(s, tm.assert_series_equal, path=setup_path)