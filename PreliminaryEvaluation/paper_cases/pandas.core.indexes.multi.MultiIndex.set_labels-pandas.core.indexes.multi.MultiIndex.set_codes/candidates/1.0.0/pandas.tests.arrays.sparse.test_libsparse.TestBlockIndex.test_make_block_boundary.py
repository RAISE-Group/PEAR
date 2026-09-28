def test_make_block_boundary(self):
    for i in [5, 10, 100, 101]:
        idx = _make_index(i, np.arange(0, i, 2, dtype=np.int32), kind='block')
        exp = np.arange(0, i, 2, dtype=np.int32)
        tm.assert_numpy_array_equal(idx.blocs, exp)
        tm.assert_numpy_array_equal(idx.blengths, np.ones(len(exp), dtype=np.int32))