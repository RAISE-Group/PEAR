def test_na_tuples(self):
    na_tuple = [(0, 1), (np.nan, np.nan), (2, 3)]
    idx_na_tuple = IntervalIndex.from_tuples(na_tuple)
    idx_na_element = IntervalIndex.from_tuples([(0, 1), np.nan, (2, 3)])
    tm.assert_index_equal(idx_na_tuple, idx_na_element)