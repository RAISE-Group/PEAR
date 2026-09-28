def test_1d_with_out(self, dtype_can_hold_na, writeable):
    dtype, can_hold_na = dtype_can_hold_na
    data = np.random.randint(0, 2, 4).astype(dtype)
    data.flags.writeable = writeable
    indexer = [2, 1, 0, 1]
    out = np.empty(4, dtype=dtype)
    algos.take_1d(data, indexer, out=out)
    expected = data.take(indexer)
    tm.assert_almost_equal(out, expected)
    indexer = [2, 1, 0, -1]
    out = np.empty(4, dtype=dtype)
    if can_hold_na:
        algos.take_1d(data, indexer, out=out)
        expected = data.take(indexer)
        expected[3] = np.nan
        tm.assert_almost_equal(out, expected)
    else:
        with pytest.raises(TypeError, match=self.fill_error):
            algos.take_1d(data, indexer, out=out)
        data.take(indexer, out=out)