def test_1d_other_dtypes(self):
    arr = np.random.randn(10).astype(np.float32)
    indexer = [1, 2, 3, -1]
    result = algos.take_1d(arr, indexer)
    expected = arr.take(indexer)
    expected[-1] = np.nan
    tm.assert_almost_equal(result, expected)