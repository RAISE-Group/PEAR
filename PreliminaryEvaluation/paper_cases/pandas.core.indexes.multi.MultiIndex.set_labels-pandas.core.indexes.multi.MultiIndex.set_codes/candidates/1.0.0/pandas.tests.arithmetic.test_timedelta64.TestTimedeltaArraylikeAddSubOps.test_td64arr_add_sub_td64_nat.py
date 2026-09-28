def test_td64arr_add_sub_td64_nat(self, box_with_array):
    box = box_with_array
    tdi = pd.TimedeltaIndex([NaT, Timedelta('1s')])
    other = np.timedelta64('NaT')
    expected = pd.TimedeltaIndex(['NaT'] * 2)
    obj = tm.box_expected(tdi, box)
    expected = tm.box_expected(expected, box)
    result = obj + other
    tm.assert_equal(result, expected)
    result = other + obj
    tm.assert_equal(result, expected)
    result = obj - other
    tm.assert_equal(result, expected)
    result = other - obj
    tm.assert_equal(result, expected)