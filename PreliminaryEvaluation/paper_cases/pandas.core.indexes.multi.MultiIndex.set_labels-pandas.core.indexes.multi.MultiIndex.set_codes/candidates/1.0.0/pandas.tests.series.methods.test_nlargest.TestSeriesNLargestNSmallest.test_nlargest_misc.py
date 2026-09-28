def test_nlargest_misc(self):
    ser = Series([3.0, np.nan, 1, 2, 5])
    tm.assert_series_equal(ser.nlargest(), ser.iloc[[4, 0, 3, 2]])
    tm.assert_series_equal(ser.nsmallest(), ser.iloc[[2, 3, 0, 4]])
    msg = 'keep must be either "first", "last"'
    with pytest.raises(ValueError, match=msg):
        ser.nsmallest(keep='invalid')
    with pytest.raises(ValueError, match=msg):
        ser.nlargest(keep='invalid')
    ser = Series([1] * 5, index=[1, 2, 3, 4, 5])
    expected_first = Series([1] * 3, index=[1, 2, 3])
    expected_last = Series([1] * 3, index=[5, 4, 3])
    result = ser.nsmallest(3)
    tm.assert_series_equal(result, expected_first)
    result = ser.nsmallest(3, keep='last')
    tm.assert_series_equal(result, expected_last)
    result = ser.nlargest(3)
    tm.assert_series_equal(result, expected_first)
    result = ser.nlargest(3, keep='last')
    tm.assert_series_equal(result, expected_last)