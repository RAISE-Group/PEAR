def test_prevent_casting(self):
    index = self.create_index()
    result = index.astype('O')
    assert result.dtype == np.object_