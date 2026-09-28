def test_outer_join_sort(self):
    left_index = Index(np.random.permutation(15))
    right_index = tm.makeDateIndex(10)
    with tm.assert_produces_warning(RuntimeWarning):
        result = left_index.join(right_index, how='outer')
    with tm.assert_produces_warning(RuntimeWarning):
        expected = right_index.astype(object).union(left_index.astype(object))
    tm.assert_index_equal(result, expected)