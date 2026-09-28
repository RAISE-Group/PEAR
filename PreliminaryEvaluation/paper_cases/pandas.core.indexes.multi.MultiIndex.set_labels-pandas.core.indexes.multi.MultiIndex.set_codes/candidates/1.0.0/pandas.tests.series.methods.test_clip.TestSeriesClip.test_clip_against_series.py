def test_clip_against_series(self):
    s = Series([1.0, 1.0, 4.0])
    lower = Series([1.0, 2.0, 3.0])
    upper = Series([1.5, 2.5, 3.5])
    tm.assert_series_equal(s.clip(lower, upper), Series([1.0, 2.0, 3.5]))
    tm.assert_series_equal(s.clip(1.5, upper), Series([1.5, 1.5, 3.5]))