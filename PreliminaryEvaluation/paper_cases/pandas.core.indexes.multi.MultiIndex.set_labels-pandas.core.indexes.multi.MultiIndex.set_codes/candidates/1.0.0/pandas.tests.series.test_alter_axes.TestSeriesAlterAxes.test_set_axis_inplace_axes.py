def test_set_axis_inplace_axes(self, axis_series):
    ser = Series(np.arange(4), index=[1, 3, 5, 7], dtype='int64')
    expected = ser.copy()
    expected.index = list('abcd')
    result = ser.copy()
    result.set_axis(list('abcd'), axis=axis_series, inplace=True)
    tm.assert_series_equal(result, expected)