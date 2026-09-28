def test_get_indexer_same_categories_different_order(self):
    ci = CategoricalIndex(['a', 'b'], categories=['a', 'b'])
    result = ci.get_indexer(CategoricalIndex(['b', 'b'], categories=['b', 'a']))
    expected = np.array([1, 1], dtype='intp')
    tm.assert_numpy_array_equal(result, expected)