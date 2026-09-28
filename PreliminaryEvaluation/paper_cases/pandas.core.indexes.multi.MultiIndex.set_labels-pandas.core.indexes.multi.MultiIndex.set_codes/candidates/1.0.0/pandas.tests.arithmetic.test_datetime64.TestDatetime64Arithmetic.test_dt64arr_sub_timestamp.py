def test_dt64arr_sub_timestamp(self, box_with_array):
    ser = pd.date_range('2014-03-17', periods=2, freq='D', tz='US/Eastern')
    ts = ser[0]
    ser = tm.box_expected(ser, box_with_array)
    delta_series = pd.Series([np.timedelta64(0, 'D'), np.timedelta64(1, 'D')])
    expected = tm.box_expected(delta_series, box_with_array)
    tm.assert_equal(ser - ts, expected)
    tm.assert_equal(ts - ser, -expected)