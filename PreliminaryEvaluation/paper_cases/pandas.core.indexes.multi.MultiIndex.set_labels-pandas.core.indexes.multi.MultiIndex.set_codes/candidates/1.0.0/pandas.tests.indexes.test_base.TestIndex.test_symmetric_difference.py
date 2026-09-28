@pytest.mark.parametrize('sort', [None, False])
def test_symmetric_difference(self, sort):
    index1 = Index([5, 2, 3, 4], name='index1')
    index2 = Index([2, 3, 4, 1])
    result = index1.symmetric_difference(index2, sort=sort)
    expected = Index([5, 1])
    assert tm.equalContents(result, expected)
    assert result.name is None
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result, expected)
    expected = index1 ^ index2
    assert tm.equalContents(result, expected)
    assert result.name is None