def test_construction_dti_with_mixed_timezones(self):
    result = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    result = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='Asia/Tokyo')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00')], tz='Asia/Tokyo', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    result = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='US/Eastern'), Timestamp('2011-08-01 10:00', tz='US/Eastern')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-08-01 10:00')], tz='US/Eastern', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    with pytest.raises(ValueError):
        DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
    msg = 'cannot be converted to datetime64'
    with pytest.raises(ValueError, match=msg):
        DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='Asia/Tokyo', name='idx')
    with pytest.raises(ValueError):
        DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='US/Eastern', name='idx')
    with pytest.raises(ValueError, match=msg):
        Index([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='Asia/Tokyo', name='idx')