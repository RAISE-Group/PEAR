def test_union_sorted(self, unions):
    idx1, idx2, expected_sorted, expected_notsorted = unions
    res1 = idx1.union(idx2, sort=None)
    tm.assert_index_equal(res1, expected_sorted, exact=True)
    res1 = idx1.union(idx2, sort=False)
    tm.assert_index_equal(res1, expected_notsorted, exact=True)
    res2 = idx2.union(idx1, sort=None)
    res3 = idx1._int64index.union(idx2, sort=None)
    tm.assert_index_equal(res2, expected_sorted, exact=True)
    tm.assert_index_equal(res3, expected_sorted)