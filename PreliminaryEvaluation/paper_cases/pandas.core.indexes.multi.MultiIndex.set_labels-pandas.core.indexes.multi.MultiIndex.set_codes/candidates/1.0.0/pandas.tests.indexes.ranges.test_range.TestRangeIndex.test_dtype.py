def test_dtype(self):
    index = self.create_index()
    assert index.dtype == np.int64