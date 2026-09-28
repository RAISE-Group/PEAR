def test_3d_with_out(self, dtype_can_hold_na):
    dtype, can_hold_na = dtype_can_hold_na
    data = np.random.randint(0, 2, (5, 4, 3)).astype(dtype)
    indexer = [2, 1, 0, 1]
    out0 = np.empty((4, 4, 3), dtype=dtype)
    out1 = np.empty((5, 4, 3), dtype=dtype)
    out2 = np.empty((5, 4, 4), dtype=dtype)
    algos.take_nd(data, indexer, out=out0, axis=0)
    algos.take_nd(data, indexer, out=out1, axis=1)
    algos.take_nd(data, indexer, out=out2, axis=2)
    expected0 = data.take(indexer, axis=0)
    expected1 = data.take(indexer, axis=1)
    expected2 = data.take(indexer, axis=2)
    tm.assert_almost_equal(out0, expected0)
    tm.assert_almost_equal(out1, expected1)
    tm.assert_almost_equal(out2, expected2)
    indexer = [2, 1, 0, -1]
    out0 = np.empty((4, 4, 3), dtype=dtype)
    out1 = np.empty((5, 4, 3), dtype=dtype)
    out2 = np.empty((5, 4, 4), dtype=dtype)
    if can_hold_na:
        algos.take_nd(data, indexer, out=out0, axis=0)
        algos.take_nd(data, indexer, out=out1, axis=1)
        algos.take_nd(data, indexer, out=out2, axis=2)
        expected0 = data.take(indexer, axis=0)
        expected1 = data.take(indexer, axis=1)
        expected2 = data.take(indexer, axis=2)
        expected0[3, :, :] = np.nan
        expected1[:, 3, :] = np.nan
        expected2[:, :, 3] = np.nan
        tm.assert_almost_equal(out0, expected0)
        tm.assert_almost_equal(out1, expected1)
        tm.assert_almost_equal(out2, expected2)
    else:
        for i, out in enumerate([out0, out1, out2]):
            with pytest.raises(TypeError, match=self.fill_error):
                algos.take_nd(data, indexer, out=out, axis=i)
            data.take(indexer, out=out, axis=i)