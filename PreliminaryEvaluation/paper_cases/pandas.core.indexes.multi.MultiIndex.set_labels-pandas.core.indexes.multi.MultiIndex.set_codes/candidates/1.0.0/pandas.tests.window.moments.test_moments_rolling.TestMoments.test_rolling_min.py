def test_rolling_min(self, raw):
    self._check_moment_func(np.min, name='min', raw=raw)
    a = pd.Series([1, 2, 3, 4, 5])
    result = a.rolling(window=100, min_periods=1).min()
    expected = pd.Series(np.ones(len(a)))
    tm.assert_series_equal(result, expected)
    with pytest.raises(ValueError):
        pd.Series([1, 2, 3]).rolling(window=3, min_periods=5).min()