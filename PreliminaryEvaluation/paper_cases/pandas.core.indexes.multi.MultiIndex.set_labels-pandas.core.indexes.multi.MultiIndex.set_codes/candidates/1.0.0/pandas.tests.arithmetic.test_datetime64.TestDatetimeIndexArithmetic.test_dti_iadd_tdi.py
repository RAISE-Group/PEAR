def test_dti_iadd_tdi(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = DatetimeIndex([Timestamp('2017-01-01', tz=tz)] * 10)
    tdi = pd.timedelta_range('0 days', periods=10)
    expected = pd.date_range('2017-01-01', periods=10, tz=tz)
    result = DatetimeIndex([Timestamp('2017-01-01', tz=tz)] * 10)
    result += tdi
    tm.assert_index_equal(result, expected)
    result = pd.timedelta_range('0 days', periods=10)
    result += dti
    tm.assert_index_equal(result, expected)
    result = DatetimeIndex([Timestamp('2017-01-01', tz=tz)] * 10)
    result += tdi.values
    tm.assert_index_equal(result, expected)
    result = pd.timedelta_range('0 days', periods=10)
    result += dti
    tm.assert_index_equal(result, expected)