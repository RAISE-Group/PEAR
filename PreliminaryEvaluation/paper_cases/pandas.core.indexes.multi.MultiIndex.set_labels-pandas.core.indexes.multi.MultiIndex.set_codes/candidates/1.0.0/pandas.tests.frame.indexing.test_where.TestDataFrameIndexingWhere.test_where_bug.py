def test_where_bug(self):
    df = DataFrame({'a': [1.0, 2.0, 3.0, 4.0], 'b': [4.0, 3.0, 2.0, 1.0]}, dtype='float64')
    expected = DataFrame({'a': [np.nan, np.nan, 3.0, 4.0], 'b': [4.0, 3.0, np.nan, np.nan]}, dtype='float64')
    result = df.where(df > 2, np.nan)
    tm.assert_frame_equal(result, expected)
    result = df.copy()
    result.where(result > 2, np.nan, inplace=True)
    tm.assert_frame_equal(result, expected)