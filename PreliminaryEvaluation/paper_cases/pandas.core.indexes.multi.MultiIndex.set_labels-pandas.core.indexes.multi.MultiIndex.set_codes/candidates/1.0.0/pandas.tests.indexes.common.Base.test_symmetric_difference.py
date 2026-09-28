def test_symmetric_difference(self, indices):
    if isinstance(indices, CategoricalIndex):
        return
    first = indices[1:]
    second = indices[:-1]
    answer = indices[[0, -1]]
    result = first.symmetric_difference(second)
    assert tm.equalContents(result, answer)
    cases = [klass(second.values) for klass in [np.array, Series, list]]
    for case in cases:
        result = first.symmetric_difference(case)
        assert tm.equalContents(result, answer)
    if isinstance(indices, MultiIndex):
        msg = 'other must be a MultiIndex or a list of tuples'
        with pytest.raises(TypeError, match=msg):
            first.symmetric_difference([1, 2, 3])