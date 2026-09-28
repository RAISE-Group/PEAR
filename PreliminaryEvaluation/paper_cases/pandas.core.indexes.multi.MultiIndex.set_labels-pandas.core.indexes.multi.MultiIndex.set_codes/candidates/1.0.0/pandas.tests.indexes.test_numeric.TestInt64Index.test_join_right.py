def test_join_right(self):
    index = self.create_index()
    other = Int64Index([7, 12, 25, 1, 2, 5])
    other_mono = Int64Index([1, 2, 5, 7, 12, 25])
    res, lidx, ridx = index.join(other, how='right', return_indexers=True)
    eres = other
    elidx = np.array([-1, 6, -1, -1, 1, -1], dtype=np.intp)
    assert isinstance(other, Int64Index)
    tm.assert_index_equal(res, eres)
    tm.assert_numpy_array_equal(lidx, elidx)
    assert ridx is None
    res, lidx, ridx = index.join(other_mono, how='right', return_indexers=True)
    eres = other_mono
    elidx = np.array([-1, 1, -1, -1, 6, -1], dtype=np.intp)
    assert isinstance(other, Int64Index)
    tm.assert_index_equal(res, eres)
    tm.assert_numpy_array_equal(lidx, elidx)
    assert ridx is None
    idx = Index([1, 1, 2, 5])
    idx2 = Index([1, 2, 5, 7, 9])
    res, lidx, ridx = idx.join(idx2, how='right', return_indexers=True)
    eres = Index([1, 1, 2, 5, 7, 9])
    elidx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
    eridx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
    tm.assert_index_equal(res, eres)
    tm.assert_numpy_array_equal(lidx, elidx)
    tm.assert_numpy_array_equal(ridx, eridx)