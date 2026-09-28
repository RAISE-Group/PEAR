def test_logical_compat(self):
    index = self.create_index()
    assert index.all() == index.values.all()
    assert index.any() == index.values.any()