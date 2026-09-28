def test_basic(self):
    arr = np.array([1, None, 'foo', -5.1, pd.NaT, np.nan])
    expected = np.array([False, True, False, False, True, True])
    self._check_behavior(arr, expected)