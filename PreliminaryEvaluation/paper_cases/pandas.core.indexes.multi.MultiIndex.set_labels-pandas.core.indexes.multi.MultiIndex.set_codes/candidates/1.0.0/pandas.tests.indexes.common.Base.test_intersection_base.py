def test_intersection_base(self, indices):
    if isinstance(indices, CategoricalIndex):
        return
    first = indices[:5]
    second = indices[:3]
    intersect = first.intersection(second)
    assert tm.equalContents(intersect, second)
    cases = [klass(second.values) for klass in [np.array, Series, list]]
    for case in cases:
        result = first.intersection(case)
        assert tm.equalContents(result, second)
    if isinstance(indices, MultiIndex):
        msg = 'other must be a MultiIndex or a list of tuples'
        with pytest.raises(TypeError, match=msg):
            first.intersection([1, 2, 3])