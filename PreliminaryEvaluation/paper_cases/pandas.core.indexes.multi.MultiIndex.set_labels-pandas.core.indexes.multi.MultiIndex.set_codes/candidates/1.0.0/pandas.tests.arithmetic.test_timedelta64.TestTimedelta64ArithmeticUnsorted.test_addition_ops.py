def test_addition_ops(self):
    tdi = TimedeltaIndex(['1 days', pd.NaT, '2 days'], name='foo')
    dti = pd.date_range('20130101', periods=3, name='bar')
    td = Timedelta('1 days')
    dt = Timestamp('20130101')
    result = tdi + dt
    expected = DatetimeIndex(['20130102', pd.NaT, '20130103'], name='foo')
    tm.assert_index_equal(result, expected)
    result = dt + tdi
    expected = DatetimeIndex(['20130102', pd.NaT, '20130103'], name='foo')
    tm.assert_index_equal(result, expected)
    result = td + tdi
    expected = TimedeltaIndex(['2 days', pd.NaT, '3 days'], name='foo')
    tm.assert_index_equal(result, expected)
    result = tdi + td
    expected = TimedeltaIndex(['2 days', pd.NaT, '3 days'], name='foo')
    tm.assert_index_equal(result, expected)
    msg = 'cannot add indices of unequal length'
    with pytest.raises(ValueError, match=msg):
        tdi + dti[0:1]
    with pytest.raises(ValueError, match=msg):
        tdi[0:1] + dti
    with pytest.raises(TypeError):
        tdi + pd.Int64Index([1, 2, 3])
    result = tdi + dti
    expected = DatetimeIndex(['20130102', pd.NaT, '20130105'])
    tm.assert_index_equal(result, expected)
    result = dti + tdi
    expected = DatetimeIndex(['20130102', pd.NaT, '20130105'])
    tm.assert_index_equal(result, expected)
    result = dt + td
    expected = Timestamp('20130102')
    assert result == expected
    result = td + dt
    expected = Timestamp('20130102')
    assert result == expected