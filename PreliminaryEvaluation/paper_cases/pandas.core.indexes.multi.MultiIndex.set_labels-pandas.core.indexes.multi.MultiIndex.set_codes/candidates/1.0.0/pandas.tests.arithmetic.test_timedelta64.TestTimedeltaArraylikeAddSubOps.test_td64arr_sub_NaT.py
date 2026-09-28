def test_td64arr_sub_NaT(self, box_with_array):
    box = box_with_array
    ser = Series([NaT, Timedelta('1s')])
    expected = Series([NaT, NaT], dtype='timedelta64[ns]')
    ser = tm.box_expected(ser, box)
    expected = tm.box_expected(expected, box)
    res = ser - pd.NaT
    tm.assert_equal(res, expected)