def test_dti_tdi_numeric_ops(self):
    tdi = TimedeltaIndex(['1 days', pd.NaT, '2 days'], name='foo')
    dti = pd.date_range('20130101', periods=3, name='bar')
    result = tdi - tdi
    expected = TimedeltaIndex(['0 days', pd.NaT, '0 days'], name='foo')
    tm.assert_index_equal(result, expected)
    result = tdi + tdi
    expected = TimedeltaIndex(['2 days', pd.NaT, '4 days'], name='foo')
    tm.assert_index_equal(result, expected)
    result = dti - tdi
    expected = DatetimeIndex(['20121231', pd.NaT, '20130101'])
    tm.assert_index_equal(result, expected)