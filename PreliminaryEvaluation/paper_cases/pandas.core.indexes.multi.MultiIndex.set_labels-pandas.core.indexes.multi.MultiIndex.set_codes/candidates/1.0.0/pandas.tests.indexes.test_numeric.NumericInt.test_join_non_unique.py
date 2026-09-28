def test_join_non_unique(self):
    left = Index([4, 4, 3, 3])
    joined, lidx, ridx = left.join(left, return_indexers=True)
    exp_joined = Index([3, 3, 3, 3, 4, 4, 4, 4])
    tm.assert_index_equal(joined, exp_joined)
    exp_lidx = np.array([2, 2, 3, 3, 0, 0, 1, 1], dtype=np.intp)
    tm.assert_numpy_array_equal(lidx, exp_lidx)
    exp_ridx = np.array([2, 3, 2, 3, 0, 1, 0, 1], dtype=np.intp)
    tm.assert_numpy_array_equal(ridx, exp_ridx)