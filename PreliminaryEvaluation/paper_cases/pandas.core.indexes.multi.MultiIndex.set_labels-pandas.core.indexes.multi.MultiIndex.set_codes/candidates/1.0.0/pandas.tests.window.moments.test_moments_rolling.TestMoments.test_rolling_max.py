def test_rolling_max(self, raw):
    self._check_moment_func(np.max, name='max', raw=raw)
    a = pd.Series([1, 2, 3, 4, 5], dtype=np.float64)
    b = a.rolling(window=100, min_periods=1).max()
    tm.assert_almost_equal(a, b)
    with pytest.raises(ValueError):
        pd.Series([1, 2, 3]).rolling(window=3, min_periods=5).max()