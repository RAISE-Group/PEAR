def test_dti_add_tdi(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = DatetimeIndex([Timestamp('2017-01-01', tz=tz)] * 10)
    tdi = pd.timedelta_range('0 days', periods=10)
    expected = pd.date_range('2017-01-01', periods=10, tz=tz)
    result = dti + tdi
    tm.assert_index_equal(result, expected)
    result = tdi + dti
    tm.assert_index_equal(result, expected)
    result = dti + tdi.values
    tm.assert_index_equal(result, expected)
    result = tdi.values + dti
    tm.assert_index_equal(result, expected)