def test_has_duplicates(self):
    idx = CategoricalIndex([0, 0, 0], name='foo')
    assert idx.is_unique is False
    assert idx.has_duplicates is True