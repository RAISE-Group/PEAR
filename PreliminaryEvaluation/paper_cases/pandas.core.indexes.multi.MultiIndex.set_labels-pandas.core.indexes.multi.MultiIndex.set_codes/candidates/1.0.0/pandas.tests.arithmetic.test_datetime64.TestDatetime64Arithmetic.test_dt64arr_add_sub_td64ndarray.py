def test_dt64arr_add_sub_td64ndarray(self, tz_naive_fixture, box_with_array):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=3, tz=tz)
    tdi = pd.TimedeltaIndex(['-1 Day', '-1 Day', '-1 Day'])
    tdarr = tdi.values
    expected = pd.date_range('2015-12-31', periods=3, tz=tz)
    dtarr = tm.box_expected(dti, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = dtarr + tdarr
    tm.assert_equal(result, expected)
    result = tdarr + dtarr
    tm.assert_equal(result, expected)
    expected = pd.date_range('2016-01-02', periods=3, tz=tz)
    expected = tm.box_expected(expected, box_with_array)
    result = dtarr - tdarr
    tm.assert_equal(result, expected)
    msg = 'cannot subtract|(bad|unsupported) operand type for unary'
    with pytest.raises(TypeError, match=msg):
        tdarr - dtarr