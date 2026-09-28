def test_td64arr_div_td64nat(self, box_with_array):
    rng = timedelta_range('1 days', '10 days')
    rng = tm.box_expected(rng, box_with_array)
    other = np.timedelta64('NaT')
    expected = np.array([np.nan] * 10)
    expected = tm.box_expected(expected, box_with_array)
    result = rng / other
    tm.assert_equal(result, expected)
    result = other / rng
    tm.assert_equal(result, expected)