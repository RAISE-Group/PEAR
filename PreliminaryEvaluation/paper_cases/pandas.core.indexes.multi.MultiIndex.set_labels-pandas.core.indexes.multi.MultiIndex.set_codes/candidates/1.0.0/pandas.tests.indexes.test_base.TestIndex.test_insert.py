def test_insert(self):
    result = Index(['b', 'c', 'd'])
    tm.assert_index_equal(Index(['a', 'b', 'c', 'd']), result.insert(0, 'a'))
    tm.assert_index_equal(Index(['b', 'c', 'e', 'd']), result.insert(-1, 'e'))
    tm.assert_index_equal(result.insert(1, 'z'), result.insert(-2, 'z'))
    null_index = Index([])
    tm.assert_index_equal(Index(['a']), null_index.insert(0, 'a'))