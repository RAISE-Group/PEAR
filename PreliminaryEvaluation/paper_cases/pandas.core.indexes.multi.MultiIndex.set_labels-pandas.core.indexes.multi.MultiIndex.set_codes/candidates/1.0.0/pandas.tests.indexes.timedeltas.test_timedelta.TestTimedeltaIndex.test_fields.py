def test_fields(self):
    rng = timedelta_range('1 days, 10:11:12.100123456', periods=2, freq='s')
    tm.assert_index_equal(rng.days, Index([1, 1], dtype='int64'))
    tm.assert_index_equal(rng.seconds, Index([10 * 3600 + 11 * 60 + 12, 10 * 3600 + 11 * 60 + 13], dtype='int64'))
    tm.assert_index_equal(rng.microseconds, Index([100 * 1000 + 123, 100 * 1000 + 123], dtype='int64'))
    tm.assert_index_equal(rng.nanoseconds, Index([456, 456], dtype='int64'))
    msg = "'TimedeltaIndex' object has no attribute '{}'"
    with pytest.raises(AttributeError, match=msg.format('hours')):
        rng.hours
    with pytest.raises(AttributeError, match=msg.format('minutes')):
        rng.minutes
    with pytest.raises(AttributeError, match=msg.format('milliseconds')):
        rng.milliseconds
    s = Series(rng)
    s[1] = np.nan
    tm.assert_series_equal(s.dt.days, Series([1, np.nan], index=[0, 1]))
    tm.assert_series_equal(s.dt.seconds, Series([10 * 3600 + 11 * 60 + 12, np.nan], index=[0, 1]))
    rng.name = 'name'
    assert rng.days.name == 'name'