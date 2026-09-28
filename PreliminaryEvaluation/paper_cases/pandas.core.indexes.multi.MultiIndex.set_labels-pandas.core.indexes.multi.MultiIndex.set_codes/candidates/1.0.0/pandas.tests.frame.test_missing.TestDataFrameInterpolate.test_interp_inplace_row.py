def test_interp_inplace_row(self):
    result = DataFrame({'a': [1.0, 2.0, 3.0, 4.0], 'b': [np.nan, 2.0, 3.0, 4.0], 'c': [3, 2, 2, 2]})
    expected = result.interpolate(method='linear', axis=1, inplace=False)
    result.interpolate(method='linear', axis=1, inplace=True)
    tm.assert_frame_equal(result, expected)