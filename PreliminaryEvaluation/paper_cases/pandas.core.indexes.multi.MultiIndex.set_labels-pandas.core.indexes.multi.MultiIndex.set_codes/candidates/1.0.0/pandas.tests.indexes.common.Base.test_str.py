def test_str(self):
    idx = self.create_index()
    idx.name = 'foo'
    assert "'foo'" in str(idx)
    assert type(idx).__name__ in str(idx)