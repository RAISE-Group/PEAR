def test_constructor_dtype(self):
    idx = DatetimeIndex(['2013-01-01', '2013-01-02'], dtype='datetime64[ns, US/Eastern]')
    expected = DatetimeIndex(['2013-01-01', '2013-01-02']).tz_localize('US/Eastern')
    tm.assert_index_equal(idx, expected)
    idx = DatetimeIndex(['2013-01-01', '2013-01-02'], tz='US/Eastern')
    tm.assert_index_equal(idx, expected)
    idx = DatetimeIndex(['2013-01-01', '2013-01-02'], dtype='datetime64[ns, US/Eastern]')
    msg = 'cannot supply both a tz and a timezone-naive dtype \\(i\\.e\\. datetime64\\[ns\\]\\)'
    with pytest.raises(ValueError, match=msg):
        DatetimeIndex(idx, dtype='datetime64[ns]')
    msg = 'data is already tz-aware US/Eastern, unable to set specified tz: CET'
    with pytest.raises(TypeError, match=msg):
        DatetimeIndex(idx, dtype='datetime64[ns, CET]')
    msg = 'cannot supply both a tz and a dtype with a tz'
    with pytest.raises(ValueError, match=msg):
        DatetimeIndex(idx, tz='CET', dtype='datetime64[ns, US/Eastern]')
    result = DatetimeIndex(idx, dtype='datetime64[ns, US/Eastern]')
    tm.assert_index_equal(idx, result)