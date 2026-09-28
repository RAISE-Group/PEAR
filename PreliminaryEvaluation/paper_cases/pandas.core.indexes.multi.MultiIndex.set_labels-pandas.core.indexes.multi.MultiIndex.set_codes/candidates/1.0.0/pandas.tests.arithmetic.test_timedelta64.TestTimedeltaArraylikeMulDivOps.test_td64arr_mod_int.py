def test_td64arr_mod_int(self, box_with_array):
    tdi = timedelta_range('1 ns', '10 ns', periods=10)
    tdarr = tm.box_expected(tdi, box_with_array)
    expected = TimedeltaIndex(['1 ns', '0 ns'] * 5)
    expected = tm.box_expected(expected, box_with_array)
    result = tdarr % 2
    tm.assert_equal(result, expected)
    with pytest.raises(TypeError):
        2 % tdarr
    if box_with_array is pd.DataFrame:
        pytest.xfail('DataFrame does not have __divmod__ or __rdivmod__')
    result = divmod(tdarr, 2)
    tm.assert_equal(result[1], expected)
    tm.assert_equal(result[0], tdarr // 2)