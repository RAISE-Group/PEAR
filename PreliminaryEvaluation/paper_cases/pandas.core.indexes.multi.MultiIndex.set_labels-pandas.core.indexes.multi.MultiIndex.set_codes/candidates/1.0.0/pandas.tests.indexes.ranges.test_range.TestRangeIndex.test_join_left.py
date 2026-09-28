def test_join_left(self):
    index = self.create_index()
    other = Int64Index(np.arange(25, 14, -1))
    res, lidx, ridx = index.join(other, how='left', return_indexers=True)
    eres = index
    eridx = np.array([-1, -1, -1, -1, -1, -1, -1, -1, 9, 7], dtype=np.intp)
    assert isinstance(res, RangeIndex)
    tm.assert_index_equal(res, eres)
    assert lidx is None
    tm.assert_numpy_array_equal(ridx, eridx)
    other = Int64Index(np.arange(25, 14, -1))
    res, lidx, ridx = index.join(other, how='left', return_indexers=True)
    assert isinstance(res, RangeIndex)
    tm.assert_index_equal(res, eres)
    assert lidx is None
    tm.assert_numpy_array_equal(ridx, eridx)