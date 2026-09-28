def test_eq_with_numpy_object(self, dtype):
    assert dtype != np.dtype('object')