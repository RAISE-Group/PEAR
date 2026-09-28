def test_map_with_tuples(self):
    index = tm.makeIntIndex(3)
    result = tm.makeIntIndex(3).map(lambda x: (x,))
    expected = Index([(i,) for i in index])
    tm.assert_index_equal(result, expected)
    result = index.map(lambda x: (x, x == 1))
    expected = MultiIndex.from_tuples([(i, i == 1) for i in index])
    tm.assert_index_equal(result, expected)