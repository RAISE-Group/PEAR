@td.skip_if_no_scipy
def test_interp_various(self):
    df = DataFrame({'A': [1, 2, np.nan, 4, 5, np.nan, 7], 'C': [1, 2, 3, 5, 8, 13, 21]})
    df = df.set_index('C')
    expected = df.copy()
    result = df.interpolate(method='polynomial', order=1)
    expected.A.loc[3] = 2.66666667
    expected.A.loc[13] = 5.76923076
    tm.assert_frame_equal(result, expected)
    result = df.interpolate(method='cubic')
    expected.A.loc[3] = 2.81547781
    expected.A.loc[13] = 5.52964175
    tm.assert_frame_equal(result, expected)
    result = df.interpolate(method='nearest')
    expected.A.loc[3] = 2
    expected.A.loc[13] = 5
    tm.assert_frame_equal(result, expected, check_dtype=False)
    result = df.interpolate(method='quadratic')
    expected.A.loc[3] = 2.82150771
    expected.A.loc[13] = 6.12648668
    tm.assert_frame_equal(result, expected)
    result = df.interpolate(method='slinear')
    expected.A.loc[3] = 2.66666667
    expected.A.loc[13] = 5.76923077
    tm.assert_frame_equal(result, expected)
    result = df.interpolate(method='zero')
    expected.A.loc[3] = 2.0
    expected.A.loc[13] = 5
    tm.assert_frame_equal(result, expected, check_dtype=False)