def test_logical_compat(self):
    idx = self.create_index()
    assert idx.all() == idx.values.all()
    assert idx.any() == idx.values.any()