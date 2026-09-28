def test_dti_sub_tdi(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = DatetimeIndex([Timestamp('2017-01-01', tz=tz)] * 10)
    tdi = pd.timedelta_range('0 days', periods=10)
    expected = pd.date_range('2017-01-01', periods=10, tz=tz, freq='-1D')
    result = dti - tdi
    tm.assert_index_equal(result, expected)
    msg = 'cannot subtract .*TimedeltaArray'
    with pytest.raises(TypeError, match=msg):
        tdi - dti
    result = dti - tdi.values
    tm.assert_index_equal(result, expected)
    msg = 'cannot subtract DatetimeArray from'
    with pytest.raises(TypeError, match=msg):
        tdi.values - dti