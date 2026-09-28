def test_factorize_dst(self):
    idx = pd.date_range('2016-11-06', freq='H', periods=12, tz='US/Eastern')
    for obj in [idx, pd.Series(idx)]:
        arr, res = obj.factorize()
        tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
        tm.assert_index_equal(res, idx)
    idx = pd.date_range('2016-06-13', freq='H', periods=12, tz='US/Eastern')
    for obj in [idx, pd.Series(idx)]:
        arr, res = obj.factorize()
        tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
        tm.assert_index_equal(res, idx)