def test_numpy_informed(self):
    with pytest.raises(TypeError, match='data type not understood'):
        np.dtype(self.dtype)
    assert not self.dtype == np.str_
    assert not np.str_ == self.dtype