def test_empty_like(self):
    arr = np.empty_like([None])
    expected = np.array([True])
    self._check_behavior(arr, expected)