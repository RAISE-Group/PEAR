def test_ensure_copied_data(self, indices):
    _base = lambda ar: ar if getattr(ar, 'base', None) is None else ar.base
    result = CategoricalIndex(indices.values, copy=True)
    tm.assert_index_equal(indices, result)
    assert _base(indices.values) is not _base(result.values)
    result = CategoricalIndex(indices.values, copy=False)
    assert _base(indices.values) is _base(result.values)