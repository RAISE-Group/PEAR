def test_dt64arr_timestamp_equality(self, box_with_array):
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    ser = pd.Series([pd.Timestamp('2000-01-29 01:59:00'), 'NaT'])
    ser = tm.box_expected(ser, box_with_array)
    result = ser != ser
    expected = tm.box_expected([False, True], xbox)
    tm.assert_equal(result, expected)
    result = ser != ser[0]
    expected = tm.box_expected([False, True], xbox)
    tm.assert_equal(result, expected)
    result = ser != ser[1]
    expected = tm.box_expected([True, True], xbox)
    tm.assert_equal(result, expected)
    result = ser == ser
    expected = tm.box_expected([True, False], xbox)
    tm.assert_equal(result, expected)
    result = ser == ser[0]
    expected = tm.box_expected([True, False], xbox)
    tm.assert_equal(result, expected)
    result = ser == ser[1]
    expected = tm.box_expected([False, False], xbox)
    tm.assert_equal(result, expected)