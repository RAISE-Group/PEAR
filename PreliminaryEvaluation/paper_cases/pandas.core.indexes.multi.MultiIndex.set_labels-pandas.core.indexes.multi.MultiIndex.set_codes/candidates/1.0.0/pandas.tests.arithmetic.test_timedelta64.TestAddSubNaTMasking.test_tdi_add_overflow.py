def test_tdi_add_overflow(self):
    with pytest.raises(OutOfBoundsDatetime):
        pd.to_timedelta(106580, 'D') + Timestamp('2000')
    with pytest.raises(OutOfBoundsDatetime):
        Timestamp('2000') + pd.to_timedelta(106580, 'D')
    _NaT = int(pd.NaT) + 1
    msg = 'Overflow in int64 addition'
    with pytest.raises(OverflowError, match=msg):
        pd.to_timedelta([106580], 'D') + Timestamp('2000')
    with pytest.raises(OverflowError, match=msg):
        Timestamp('2000') + pd.to_timedelta([106580], 'D')
    with pytest.raises(OverflowError, match=msg):
        pd.to_timedelta([_NaT]) - Timedelta('1 days')
    with pytest.raises(OverflowError, match=msg):
        pd.to_timedelta(['5 days', _NaT]) - Timedelta('1 days')
    with pytest.raises(OverflowError, match=msg):
        pd.to_timedelta([_NaT, '5 days', '1 hours']) - pd.to_timedelta(['7 seconds', _NaT, '4 hours'])
    exp = TimedeltaIndex([pd.NaT])
    result = pd.to_timedelta([pd.NaT]) - Timedelta('1 days')
    tm.assert_index_equal(result, exp)
    exp = TimedeltaIndex(['4 days', pd.NaT])
    result = pd.to_timedelta(['5 days', pd.NaT]) - Timedelta('1 days')
    tm.assert_index_equal(result, exp)
    exp = TimedeltaIndex([pd.NaT, pd.NaT, '5 hours'])
    result = pd.to_timedelta([pd.NaT, '5 days', '1 hours']) + pd.to_timedelta(['7 seconds', pd.NaT, '4 hours'])
    tm.assert_index_equal(result, exp)