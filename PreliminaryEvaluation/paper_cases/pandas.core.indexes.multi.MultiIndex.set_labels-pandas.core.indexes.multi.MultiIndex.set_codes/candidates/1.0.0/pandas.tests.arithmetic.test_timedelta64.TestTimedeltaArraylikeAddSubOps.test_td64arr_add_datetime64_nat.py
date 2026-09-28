def test_td64arr_add_datetime64_nat(self, box_with_array):
    other = np.datetime64('NaT')
    tdi = timedelta_range('1 day', periods=3)
    expected = pd.DatetimeIndex(['NaT', 'NaT', 'NaT'])
    tdser = tm.box_expected(tdi, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(tdser + other, expected)
    tm.assert_equal(other + tdser, expected)