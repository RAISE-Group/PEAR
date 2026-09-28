def test_argsort(self):
    index = self.create_index()
    with pytest.raises(TypeError, match="'>|<' not supported"):
        index.argsort()