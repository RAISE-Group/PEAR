def test_to_series(self):
    idx = self.create_index()
    s = idx.to_series()
    assert s.values is not idx.values
    assert s.index is not idx
    assert s.name == idx.name