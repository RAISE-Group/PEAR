def test_interp_pad_datetime64tz_values(self):
    dti = pd.date_range('2015-04-05', periods=3, tz='US/Central')
    ser = pd.Series(dti)
    ser[1] = pd.NaT
    result = ser.interpolate(method='pad')
    expected = pd.Series(dti)
    expected[1] = expected[0]
    tm.assert_series_equal(result, expected)