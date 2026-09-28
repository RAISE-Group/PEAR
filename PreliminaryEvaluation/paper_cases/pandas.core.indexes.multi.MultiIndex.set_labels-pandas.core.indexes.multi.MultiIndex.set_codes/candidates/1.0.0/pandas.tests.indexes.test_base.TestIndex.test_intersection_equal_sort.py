def test_intersection_equal_sort(self):
    idx = pd.Index(['c', 'a', 'b'])
    tm.assert_index_equal(idx.intersection(idx, sort=False), idx)
    tm.assert_index_equal(idx.intersection(idx, sort=None), idx)