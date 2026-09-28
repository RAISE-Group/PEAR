@pytest.mark.parametrize('pos,expected', [(0, Index(['b', 'c', 'd'], name='index')), (-1, Index(['a', 'b', 'c'], name='index'))])
def test_delete(self, pos, expected):
    index = Index(['a', 'b', 'c', 'd'], name='index')
    result = index.delete(pos)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name