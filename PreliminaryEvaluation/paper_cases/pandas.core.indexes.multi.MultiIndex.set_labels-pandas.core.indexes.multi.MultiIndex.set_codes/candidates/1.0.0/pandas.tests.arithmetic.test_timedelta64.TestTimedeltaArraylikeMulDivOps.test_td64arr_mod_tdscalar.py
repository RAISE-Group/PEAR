def test_td64arr_mod_tdscalar(self, box_with_array, three_days):
    tdi = timedelta_range('1 Day', '9 days')
    tdarr = tm.box_expected(tdi, box_with_array)
    expected = TimedeltaIndex(['1 Day', '2 Days', '0 Days'] * 3)
    expected = tm.box_expected(expected, box_with_array)
    result = tdarr % three_days
    tm.assert_equal(result, expected)
    if box_with_array is pd.DataFrame:
        pytest.xfail('DataFrame does not have __divmod__ or __rdivmod__')
    result = divmod(tdarr, three_days)
    tm.assert_equal(result[1], expected)
    tm.assert_equal(result[0], tdarr // three_days)