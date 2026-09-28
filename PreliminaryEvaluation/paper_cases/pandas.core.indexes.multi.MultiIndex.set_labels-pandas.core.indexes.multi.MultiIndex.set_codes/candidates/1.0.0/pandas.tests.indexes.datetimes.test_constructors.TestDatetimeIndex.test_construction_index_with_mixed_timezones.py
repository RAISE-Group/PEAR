def test_construction_index_with_mixed_timezones(self):
    result = Index([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    assert result.tz is None
    result = Index([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='Asia/Tokyo')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00')], tz='Asia/Tokyo', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    assert result.tz is not None
    assert result.tz == exp.tz
    result = Index([Timestamp('2011-01-01 10:00', tz='US/Eastern'), Timestamp('2011-08-01 10:00', tz='US/Eastern')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-08-01 10:00')], tz='US/Eastern', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    assert result.tz is not None
    assert result.tz == exp.tz
    result = Index([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
    exp = Index([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='object', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert not isinstance(result, DatetimeIndex)
    result = Index([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
    exp = Index([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='object', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert not isinstance(result, DatetimeIndex)
    result = Index([Timestamp('2011-01-01')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01')], name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    assert result.tz is None
    result = Index([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo')], name='idx')
    exp = DatetimeIndex([Timestamp('2011-01-01 10:00')], tz='Asia/Tokyo', name='idx')
    tm.assert_index_equal(result, exp, exact=True)
    assert isinstance(result, DatetimeIndex)
    assert result.tz is not None
    assert result.tz == exp.tz