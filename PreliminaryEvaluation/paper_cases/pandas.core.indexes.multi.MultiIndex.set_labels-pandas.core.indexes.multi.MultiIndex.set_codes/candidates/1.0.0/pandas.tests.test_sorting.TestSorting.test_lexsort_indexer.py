def test_lexsort_indexer(self):
    keys = [[np.nan] * 5 + list(range(100)) + [np.nan] * 5]
    result = lexsort_indexer(keys, orders=True, na_position='last')
    exp = list(range(5, 105)) + list(range(5)) + list(range(105, 110))
    tm.assert_numpy_array_equal(result, np.array(exp, dtype=np.intp))
    result = lexsort_indexer(keys, orders=True, na_position='first')
    exp = list(range(5)) + list(range(105, 110)) + list(range(5, 105))
    tm.assert_numpy_array_equal(result, np.array(exp, dtype=np.intp))
    result = lexsort_indexer(keys, orders=False, na_position='last')
    exp = list(range(104, 4, -1)) + list(range(5)) + list(range(105, 110))
    tm.assert_numpy_array_equal(result, np.array(exp, dtype=np.intp))
    result = lexsort_indexer(keys, orders=False, na_position='first')
    exp = list(range(5)) + list(range(105, 110)) + list(range(104, 4, -1))
    tm.assert_numpy_array_equal(result, np.array(exp, dtype=np.intp))