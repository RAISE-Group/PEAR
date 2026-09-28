@pytest.mark.parametrize('sort', [None, False])
def test_intersection_equal(self, sort):
    first = timedelta_range('1 day', periods=4, freq='h')
    second = timedelta_range('1 day', periods=4, freq='h')
    intersect = first.intersection(second, sort=sort)
    if sort is None:
        tm.assert_index_equal(intersect, second.sort_values())
    assert tm.equalContents(intersect, second)
    inter = first.intersection(first, sort=sort)
    assert inter is first