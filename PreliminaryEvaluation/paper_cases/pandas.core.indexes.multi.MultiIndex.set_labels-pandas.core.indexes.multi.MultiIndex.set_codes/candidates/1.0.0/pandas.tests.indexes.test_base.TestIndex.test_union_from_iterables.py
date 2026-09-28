@pytest.mark.parametrize('klass', [np.array, Series, list])
@pytest.mark.parametrize('sort', [None, False])
def test_union_from_iterables(self, index, klass, sort):
    first = index[5:20]
    second = index[:10]
    everything = index[:20]
    case = klass(second.values)
    result = first.union(case, sort=sort)
    if sort is None:
        tm.assert_index_equal(result, everything.sort_values())
    assert tm.equalContents(result, everything)