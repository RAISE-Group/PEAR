@pytest.mark.parametrize('sort', [None, False])
def test_symmetric_difference_non_index(self, sort):
    index1 = Index([1, 2, 3, 4], name='index1')
    index2 = np.array([2, 3, 4, 5])
    expected = Index([1, 5])
    result = index1.symmetric_difference(index2, sort=sort)
    assert tm.equalContents(result, expected)
    assert result.name == 'index1'
    result = index1.symmetric_difference(index2, result_name='new_name', sort=sort)
    assert tm.equalContents(result, expected)
    assert result.name == 'new_name'