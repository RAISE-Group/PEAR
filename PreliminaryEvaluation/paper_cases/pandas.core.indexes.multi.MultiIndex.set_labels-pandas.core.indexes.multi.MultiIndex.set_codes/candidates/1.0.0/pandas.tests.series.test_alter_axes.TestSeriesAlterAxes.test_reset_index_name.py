def test_reset_index_name(self):
    s = Series([1, 2, 3], index=Index(range(3), name='x'))
    assert s.reset_index().index.name is None
    assert s.reset_index(drop=True).index.name is None