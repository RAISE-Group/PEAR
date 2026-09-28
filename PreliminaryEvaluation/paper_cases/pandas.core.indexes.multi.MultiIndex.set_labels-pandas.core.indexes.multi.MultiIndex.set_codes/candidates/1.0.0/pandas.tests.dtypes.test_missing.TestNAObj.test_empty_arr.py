def test_empty_arr(self):
    arr = np.array([])
    expected = np.array([], dtype=bool)
    self._check_behavior(arr, expected)