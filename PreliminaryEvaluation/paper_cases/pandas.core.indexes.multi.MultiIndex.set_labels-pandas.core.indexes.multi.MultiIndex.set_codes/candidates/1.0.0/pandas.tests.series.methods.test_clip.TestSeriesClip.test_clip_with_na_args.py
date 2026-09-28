def test_clip_with_na_args(self):
    """Should process np.nan argument as None """
    s = Series([1, 2, 3])
    tm.assert_series_equal(s.clip(np.nan), Series([1, 2, 3]))
    tm.assert_series_equal(s.clip(upper=np.nan, lower=np.nan), Series([1, 2, 3]))
    tm.assert_series_equal(s.clip(lower=[0, 4, np.nan]), Series([1, 4, np.nan]))
    tm.assert_series_equal(s.clip(upper=[1, np.nan, 1]), Series([1, np.nan, 1]))