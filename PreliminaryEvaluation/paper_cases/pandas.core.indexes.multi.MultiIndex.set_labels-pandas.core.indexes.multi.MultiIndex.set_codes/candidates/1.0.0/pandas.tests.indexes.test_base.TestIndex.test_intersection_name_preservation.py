@pytest.mark.parametrize('index2,keeps_name', [(Index([3, 4, 5, 6, 7], name='index'), True), (Index([3, 4, 5, 6, 7], name='other'), False), (Index([3, 4, 5, 6, 7]), False)])
@pytest.mark.parametrize('sort', [None, False])
def test_intersection_name_preservation(self, index2, keeps_name, sort):
    index1 = Index([1, 2, 3, 4, 5], name='index')
    expected = Index([3, 4, 5])
    result = index1.intersection(index2, sort)
    if keeps_name:
        expected.name = 'index'
    assert result.name == expected.name
    tm.assert_index_equal(result, expected)