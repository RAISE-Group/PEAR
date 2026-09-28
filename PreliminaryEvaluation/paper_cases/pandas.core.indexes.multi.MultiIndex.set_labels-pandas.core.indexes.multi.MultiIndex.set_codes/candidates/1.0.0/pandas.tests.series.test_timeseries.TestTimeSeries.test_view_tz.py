def test_view_tz(self):
    ser = pd.Series(pd.date_range('2000', periods=4, tz='US/Central'))
    result = ser.view('i8')
    expected = pd.Series([946706400000000000, 946792800000000000, 946879200000000000, 946965600000000000])
    tm.assert_series_equal(result, expected)