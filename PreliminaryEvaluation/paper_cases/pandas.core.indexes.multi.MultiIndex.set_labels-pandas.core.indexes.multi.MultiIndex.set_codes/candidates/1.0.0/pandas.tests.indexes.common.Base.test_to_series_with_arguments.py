def test_to_series_with_arguments(self):
    idx = self.create_index()
    s = idx.to_series(index=idx)
    assert s.values is not idx.values
    assert s.index is idx
    assert s.name == idx.name
    idx = self.create_index()
    s = idx.to_series(name='__test')
    assert s.values is not idx.values
    assert s.index is not idx
    assert s.name != idx.name