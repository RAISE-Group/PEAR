def test_empty(self):
    index = self.create_index()
    assert not index.empty
    assert index[:0].empty