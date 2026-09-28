def test_dt64arr_add_sub_td64_nat(self, box_with_array, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('1994-04-01', periods=9, tz=tz, freq='QS')
    other = np.timedelta64('NaT')
    expected = pd.DatetimeIndex(['NaT'] * 9, tz=tz)
    obj = tm.box_expected(dti, box_with_array, transpose=False)
    expected = tm.box_expected(expected, box_with_array, transpose=False)
    result = obj + other
    tm.assert_equal(result, expected)
    result = other + obj
    tm.assert_equal(result, expected)
    result = obj - other
    tm.assert_equal(result, expected)
    msg = 'cannot subtract'
    with pytest.raises(TypeError, match=msg):
        other - obj