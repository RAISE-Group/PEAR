@pytest.mark.parametrize('sort', [None, False])
def test_union(self, index, sort):
    first = index[5:20]
    second = index[:10]
    everything = index[:20]
    union = first.union(second, sort=sort)
    if sort is None:
        tm.assert_index_equal(union, everything.sort_values())
    assert tm.equalContents(union, everything)