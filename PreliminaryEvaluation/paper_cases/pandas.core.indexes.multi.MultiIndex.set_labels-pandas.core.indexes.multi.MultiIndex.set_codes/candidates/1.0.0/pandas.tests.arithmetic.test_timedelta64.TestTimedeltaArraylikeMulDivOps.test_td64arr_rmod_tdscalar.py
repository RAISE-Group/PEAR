def test_td64arr_rmod_tdscalar(self, box_with_array, three_days):
    tdi = timedelta_range('1 Day', '9 days')
    tdarr = tm.box_expected(tdi, box_with_array)
    expected = ['0 Days', '1 Day', '0 Days'] + ['3 Days'] * 6
    expected = TimedeltaIndex(expected)
    expected = tm.box_expected(expected, box_with_array)
    result = three_days % tdarr
    tm.assert_equal(result, expected)
    if box_with_array is pd.DataFrame:
        pytest.xfail('DataFrame does not have __divmod__ or __rdivmod__')
    result = divmod(three_days, tdarr)
    tm.assert_equal(result[1], expected)
    tm.assert_equal(result[0], three_days // tdarr)