def test_constructor_numpy_scalar(self):
    result = Series(np.array(100), index=np.arange(4), dtype='int64')
    expected = Series(100, index=np.arange(4), dtype='int64')
    tm.assert_series_equal(result, expected)