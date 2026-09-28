def test_getitem(self):
    assert self.factor[0] == 'a'
    assert self.factor[-1] == 'c'
    subf = self.factor[[0, 1, 2]]
    tm.assert_numpy_array_equal(subf._codes, np.array([0, 1, 1], dtype=np.int8))
    subf = self.factor[np.asarray(self.factor) == 'c']
    tm.assert_numpy_array_equal(subf._codes, np.array([2, 2, 2], dtype=np.int8))