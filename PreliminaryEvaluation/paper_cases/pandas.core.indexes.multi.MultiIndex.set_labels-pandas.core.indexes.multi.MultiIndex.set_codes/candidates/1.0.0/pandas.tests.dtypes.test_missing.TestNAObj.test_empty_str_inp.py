def test_empty_str_inp(self):
    arr = np.array([''])
    expected = np.array([False])
    self._check_behavior(arr, expected)