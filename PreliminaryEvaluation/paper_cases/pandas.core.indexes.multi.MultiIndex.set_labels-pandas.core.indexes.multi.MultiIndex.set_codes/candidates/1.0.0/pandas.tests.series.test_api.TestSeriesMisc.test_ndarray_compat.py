def test_ndarray_compat(self):
    tsdf = DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'], index=date_range('1/1/2000', periods=1000))

    def f(x):
        return x[x.idxmax()]
    result = tsdf.apply(f)
    expected = tsdf.max()
    tm.assert_series_equal(result, expected)
    s = Series(np.random.randn(10))
    result = Series(np.ones_like(s))
    expected = Series(1, index=range(10), dtype='float64')
    tm.assert_series_equal(result, expected)
    s = Series(np.random.randn(10))
    tm.assert_almost_equal(s.ravel(order='F'), s.values.ravel(order='F'))