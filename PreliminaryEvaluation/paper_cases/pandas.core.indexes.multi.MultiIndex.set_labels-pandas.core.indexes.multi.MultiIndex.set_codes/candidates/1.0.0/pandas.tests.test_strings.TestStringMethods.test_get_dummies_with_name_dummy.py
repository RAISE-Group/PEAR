def test_get_dummies_with_name_dummy(self):
    s = Series(['a', 'b,name', 'b'])
    result = s.str.get_dummies(',')
    expected = DataFrame([[1, 0, 0], [0, 1, 1], [0, 1, 0]], columns=['a', 'b', 'name'])
    tm.assert_frame_equal(result, expected)
    idx = Index(['a|b', 'name|c', 'b|name'])
    result = idx.str.get_dummies('|')
    expected = MultiIndex.from_tuples([(1, 1, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1)], names=('a', 'b', 'c', 'name'))
    tm.assert_index_equal(result, expected)