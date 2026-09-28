def test_constructor_name_unhashable(self):
    idx = self.create_index()
    with pytest.raises(TypeError, match='Index.name must be a hashable type'):
        type(idx)(idx, name=[])