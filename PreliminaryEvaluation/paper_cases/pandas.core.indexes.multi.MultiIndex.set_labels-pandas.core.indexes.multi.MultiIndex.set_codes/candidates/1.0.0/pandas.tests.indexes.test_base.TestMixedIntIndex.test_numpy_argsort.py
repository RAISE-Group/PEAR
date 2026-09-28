def test_numpy_argsort(self):
    index = self.create_index()
    with pytest.raises(TypeError, match="'>|<' not supported"):
        np.argsort(index)