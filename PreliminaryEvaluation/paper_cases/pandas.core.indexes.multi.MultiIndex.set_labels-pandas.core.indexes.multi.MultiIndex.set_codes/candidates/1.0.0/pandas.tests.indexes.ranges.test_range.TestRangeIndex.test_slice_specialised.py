def test_slice_specialised(self):
    index = self.create_index()
    index.name = 'foo'
    res = index[1]
    expected = 2
    assert res == expected
    res = index[-1]
    expected = 18
    assert res == expected
    index_slice = index[:]
    expected = index
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[7:10:2]
    expected = Index(np.array([14, 18]), name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[-1:-5:-2]
    expected = Index(np.array([18, 14]), name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[2:100:4]
    expected = Index(np.array([4, 12]), name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[::-1]
    expected = Index(index.values[::-1], name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[-8::-1]
    expected = Index(np.array([4, 2, 0]), name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[-40::-1]
    expected = Index(np.array([], dtype=np.int64), name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[40::-1]
    expected = Index(index.values[40::-1], name='foo')
    tm.assert_index_equal(index_slice, expected)
    index_slice = index[10::-1]
    expected = Index(index.values[::-1], name='foo')
    tm.assert_index_equal(index_slice, expected)