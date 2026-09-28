def test_concat_multiple_frames_dtypes(self):
    A = DataFrame(data=np.ones((10, 2)), columns=['foo', 'bar'], dtype=np.float64)
    B = DataFrame(data=np.ones((10, 2)), dtype=np.float32)
    results = pd.concat((A, B), axis=1).dtypes
    expected = Series([np.dtype('float64')] * 2 + [np.dtype('float32')] * 2, index=['foo', 'bar', 0, 1])
    tm.assert_series_equal(results, expected)