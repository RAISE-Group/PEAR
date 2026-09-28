def test_equals(self, indices):
    if isinstance(indices, IntervalIndex):
        return
    assert indices.equals(indices)
    assert indices.equals(indices.copy())
    assert indices.equals(indices.astype(object))
    assert not indices.equals(list(indices))
    assert not indices.equals(np.array(indices))
    if not isinstance(indices, RangeIndex):
        same_values = Index(indices, dtype=object)
        assert indices.equals(same_values)
        assert same_values.equals(indices)
    if indices.nlevels == 1:
        assert not indices.equals(Series(indices))