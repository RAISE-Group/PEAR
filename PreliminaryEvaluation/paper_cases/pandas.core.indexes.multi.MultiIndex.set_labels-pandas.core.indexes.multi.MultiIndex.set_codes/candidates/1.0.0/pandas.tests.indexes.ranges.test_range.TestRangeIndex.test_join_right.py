def test_join_right(self):
    index = self.create_index()
    other = Int64Index(np.arange(25, 14, -1))
    res, lidx, ridx = index.join(other, how='right', return_indexers=True)
    eres = other
    elidx = np.array([-1, -1, -1, -1, -1, -1, -1, 9, -1, 8, -1], dtype=np.intp)
    assert isinstance(other, Int64Index)
    tm.assert_index_equal(res, eres)
    tm.assert_numpy_array_equal(lidx, elidx)
    assert ridx is None
    other = RangeIndex(25, 14, -1)
    res, lidx, ridx = index.join(other, how='right', return_indexers=True)
    eres = other
    assert isinstance(other, RangeIndex)
    tm.assert_index_equal(res, eres)
    tm.assert_numpy_array_equal(lidx, elidx)
    assert ridx is None