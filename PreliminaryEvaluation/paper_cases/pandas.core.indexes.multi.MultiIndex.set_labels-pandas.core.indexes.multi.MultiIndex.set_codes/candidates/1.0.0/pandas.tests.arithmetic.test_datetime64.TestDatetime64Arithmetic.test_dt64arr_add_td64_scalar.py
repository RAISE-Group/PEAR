def test_dt64arr_add_td64_scalar(self, box_with_array):
    ser = Series([Timestamp('20130101 9:01'), Timestamp('20130101 9:02')])
    expected = Series([Timestamp('20130101 9:01:01'), Timestamp('20130101 9:02:01')])
    dtarr = tm.box_expected(ser, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = dtarr + np.timedelta64(1, 's')
    tm.assert_equal(result, expected)
    result = np.timedelta64(1, 's') + dtarr
    tm.assert_equal(result, expected)
    expected = Series([Timestamp('20130101 9:01:00.005'), Timestamp('20130101 9:02:00.005')])
    expected = tm.box_expected(expected, box_with_array)
    result = dtarr + np.timedelta64(5, 'ms')
    tm.assert_equal(result, expected)
    result = np.timedelta64(5, 'ms') + dtarr
    tm.assert_equal(result, expected)