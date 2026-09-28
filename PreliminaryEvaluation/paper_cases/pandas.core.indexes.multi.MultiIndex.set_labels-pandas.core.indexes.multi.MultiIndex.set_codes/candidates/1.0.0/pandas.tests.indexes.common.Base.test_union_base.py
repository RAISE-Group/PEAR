def test_union_base(self, indices):
    first = indices[3:]
    second = indices[:5]
    everything = indices
    union = first.union(second)
    assert tm.equalContents(union, everything)
    cases = [klass(second.values) for klass in [np.array, Series, list]]
    for case in cases:
        if not isinstance(indices, CategoricalIndex):
            result = first.union(case)
            assert tm.equalContents(result, everything)
    if isinstance(indices, MultiIndex):
        msg = 'other must be a MultiIndex or a list of tuples'
        with pytest.raises(TypeError, match=msg):
            first.union([1, 2, 3])