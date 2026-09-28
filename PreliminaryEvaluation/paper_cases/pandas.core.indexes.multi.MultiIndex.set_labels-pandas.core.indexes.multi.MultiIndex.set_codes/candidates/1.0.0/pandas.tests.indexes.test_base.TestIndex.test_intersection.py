@pytest.mark.parametrize('sort', [None, False])
def test_intersection(self, index, sort):
    first = index[:20]
    second = index[:10]
    intersect = first.intersection(second, sort=sort)
    if sort is None:
        tm.assert_index_equal(intersect, second.sort_values())
    assert tm.equalContents(intersect, second)
    inter = first.intersection(first, sort=sort)
    assert inter is first