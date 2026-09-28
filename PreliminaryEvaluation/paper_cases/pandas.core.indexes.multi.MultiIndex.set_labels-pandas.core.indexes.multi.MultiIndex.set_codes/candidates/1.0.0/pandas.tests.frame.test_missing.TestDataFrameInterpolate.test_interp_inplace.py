def test_interp_inplace(self):
    df = DataFrame({'a': [1.0, 2.0, np.nan, 4.0]})
    expected = DataFrame({'a': [1.0, 2.0, 3.0, 4.0]})
    result = df.copy()
    result['a'].interpolate(inplace=True)
    tm.assert_frame_equal(result, expected)
    result = df.copy()
    result['a'].interpolate(inplace=True, downcast='infer')
    tm.assert_frame_equal(result, expected.astype('int64'))