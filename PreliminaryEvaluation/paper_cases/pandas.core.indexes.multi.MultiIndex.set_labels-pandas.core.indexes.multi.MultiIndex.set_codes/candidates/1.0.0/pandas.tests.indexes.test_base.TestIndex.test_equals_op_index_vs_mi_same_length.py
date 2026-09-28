def test_equals_op_index_vs_mi_same_length(self):
    mi = MultiIndex.from_tuples([(1, 2), (4, 5), (8, 9)])
    index = Index(['foo', 'bar', 'baz'])
    result = mi == index
    expected = np.array([False, False, False])
    tm.assert_numpy_array_equal(result, expected)