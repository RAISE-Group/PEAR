def test_fillna_dtype_conversion(self):
    df = DataFrame(index=['A', 'B', 'C'], columns=[1, 2, 3, 4, 5])
    result = df.dtypes
    expected = Series([np.dtype('object')] * 5, index=[1, 2, 3, 4, 5])
    tm.assert_series_equal(result, expected)
    result = df.fillna(1)
    expected = DataFrame(1, index=['A', 'B', 'C'], columns=[1, 2, 3, 4, 5])
    tm.assert_frame_equal(result, expected)
    df = DataFrame(index=range(3), columns=['A', 'B'], dtype='float64')
    result = df.fillna('nan')
    expected = DataFrame('nan', index=range(3), columns=['A', 'B'])
    tm.assert_frame_equal(result, expected)
    df = DataFrame(dict(A=[1, np.nan], B=[1.0, 2.0]))
    for v in ['', 1, np.nan, 1.0]:
        expected = df.replace(np.nan, v)
        result = df.fillna(v)
        tm.assert_frame_equal(result, expected)