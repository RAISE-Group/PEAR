def test_subtraction_ops_with_tz(self):
    dti = pd.date_range('20130101', periods=3)
    ts = Timestamp('20130101')
    dt = ts.to_pydatetime()
    dti_tz = pd.date_range('20130101', periods=3).tz_localize('US/Eastern')
    ts_tz = Timestamp('20130101').tz_localize('US/Eastern')
    ts_tz2 = Timestamp('20130101').tz_localize('CET')
    dt_tz = ts_tz.to_pydatetime()
    td = Timedelta('1 days')

    def _check(result, expected):
        assert result == expected
        assert isinstance(result, Timedelta)
    result = ts - ts
    expected = Timedelta('0 days')
    _check(result, expected)
    result = dt_tz - ts_tz
    expected = Timedelta('0 days')
    _check(result, expected)
    result = ts_tz - dt_tz
    expected = Timedelta('0 days')
    _check(result, expected)
    msg = 'Timestamp subtraction must have the same timezones or no timezones'
    with pytest.raises(TypeError, match=msg):
        dt_tz - ts
    msg = "can't subtract offset-naive and offset-aware datetimes"
    with pytest.raises(TypeError, match=msg):
        dt_tz - dt
    msg = 'Timestamp subtraction must have the same timezones or no timezones'
    with pytest.raises(TypeError, match=msg):
        dt_tz - ts_tz2
    msg = "can't subtract offset-naive and offset-aware datetimes"
    with pytest.raises(TypeError, match=msg):
        dt - dt_tz
    msg = 'Timestamp subtraction must have the same timezones or no timezones'
    with pytest.raises(TypeError, match=msg):
        ts - dt_tz
    with pytest.raises(TypeError, match=msg):
        ts_tz2 - ts
    with pytest.raises(TypeError, match=msg):
        ts_tz2 - dt
    with pytest.raises(TypeError, match=msg):
        ts_tz - ts_tz2
    with pytest.raises(TypeError, match=msg):
        dti - ts_tz
    with pytest.raises(TypeError, match=msg):
        dti_tz - ts
    with pytest.raises(TypeError, match=msg):
        dti_tz - ts_tz2
    result = dti_tz - dt_tz
    expected = TimedeltaIndex(['0 days', '1 days', '2 days'])
    tm.assert_index_equal(result, expected)
    result = dt_tz - dti_tz
    expected = TimedeltaIndex(['0 days', '-1 days', '-2 days'])
    tm.assert_index_equal(result, expected)
    result = dti_tz - ts_tz
    expected = TimedeltaIndex(['0 days', '1 days', '2 days'])
    tm.assert_index_equal(result, expected)
    result = ts_tz - dti_tz
    expected = TimedeltaIndex(['0 days', '-1 days', '-2 days'])
    tm.assert_index_equal(result, expected)
    result = td - td
    expected = Timedelta('0 days')
    _check(result, expected)
    result = dti_tz - td
    expected = DatetimeIndex(['20121231', '20130101', '20130102'], tz='US/Eastern')
    tm.assert_index_equal(result, expected)