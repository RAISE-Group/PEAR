def test_dt64arr_sub_NaT(self, box_with_array):
    dti = pd.DatetimeIndex([pd.NaT, pd.Timestamp('19900315')])
    ser = tm.box_expected(dti, box_with_array)
    result = ser - pd.NaT
    expected = pd.Series([pd.NaT, pd.NaT], dtype='timedelta64[ns]')
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(result, expected)
    dti_tz = dti.tz_localize('Asia/Tokyo')
    ser_tz = tm.box_expected(dti_tz, box_with_array)
    result = ser_tz - pd.NaT
    expected = pd.Series([pd.NaT, pd.NaT], dtype='timedelta64[ns]')
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(result, expected)