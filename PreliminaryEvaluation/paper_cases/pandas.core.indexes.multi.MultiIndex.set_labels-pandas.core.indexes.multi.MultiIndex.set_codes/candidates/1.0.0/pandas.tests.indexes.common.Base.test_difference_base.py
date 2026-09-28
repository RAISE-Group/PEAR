@pytest.mark.parametrize('sort', [None, False])
def test_difference_base(self, sort, indices):
    if isinstance(indices, CategoricalIndex):
        return
    first = indices[2:]
    second = indices[:4]
    answer = indices[4:]
    result = first.difference(second, sort)
    assert tm.equalContents(result, answer)
    cases = [klass(second.values) for klass in [np.array, Series, list]]
    for case in cases:
        if isinstance(indices, (DatetimeIndex, TimedeltaIndex)):
            assert type(result) == type(answer)
            tm.assert_numpy_array_equal(result.sort_values().asi8, answer.sort_values().asi8)
        else:
            result = first.difference(case, sort)
            assert tm.equalContents(result, answer)
    if isinstance(indices, MultiIndex):
        msg = 'other must be a MultiIndex or a list of tuples'
        with pytest.raises(TypeError, match=msg):
            first.difference([1, 2, 3], sort)