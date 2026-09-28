def test_expanding_apply_empty_series(self, raw):
    ser = Series([], dtype=np.float64)
    tm.assert_series_equal(ser, ser.expanding().apply(lambda x: x.mean(), raw=raw))