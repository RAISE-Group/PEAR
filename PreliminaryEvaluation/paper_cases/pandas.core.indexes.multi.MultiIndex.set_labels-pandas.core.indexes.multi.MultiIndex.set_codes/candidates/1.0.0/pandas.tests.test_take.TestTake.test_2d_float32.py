def test_2d_float32(self):
    arr = np.random.randn(4, 3).astype(np.float32)
    indexer = [0, 2, -1, 1, -1]
    result = algos.take_nd(arr, indexer, axis=0)
    result2 = np.empty_like(result)
    algos.take_nd(arr, indexer, axis=0, out=result2)
    tm.assert_almost_equal(result, result2)
    expected = arr.take(indexer, axis=0)
    expected[[2, 4], :] = np.nan
    tm.assert_almost_equal(result, expected)
    out = np.empty((len(indexer), arr.shape[1]), dtype='float32')
    algos.take_nd(arr, indexer, out=out)
    result = algos.take_nd(arr, indexer, axis=1)
    result2 = np.empty_like(result)
    algos.take_nd(arr, indexer, axis=1, out=result2)
    tm.assert_almost_equal(result, result2)
    expected = arr.take(indexer, axis=1)
    expected[:, [2, 4]] = np.nan
    tm.assert_almost_equal(result, expected)