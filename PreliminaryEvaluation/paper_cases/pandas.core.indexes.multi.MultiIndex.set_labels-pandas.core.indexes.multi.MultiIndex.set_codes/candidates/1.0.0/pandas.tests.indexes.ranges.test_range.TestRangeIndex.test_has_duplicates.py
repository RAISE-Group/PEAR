def test_has_duplicates(self, indices):
    assert indices.is_unique
    assert not indices.has_duplicates