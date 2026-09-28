def test_sub_dti_dti(self):
    dti = date_range('20130101', periods=3)
    dti_tz = date_range('20130101', periods=3).tz_localize('US/Eastern')
    dti_tz2 = date_range('20130101', periods=3).tz_localize('UTC')
    expected = TimedeltaIndex([0, 0, 0])
    result = dti - dti
    tm.assert_index_equal(result, expected)
    result = dti_tz - dti_tz
    tm.assert_index_equal(result, expected)
    msg = 'DatetimeArray subtraction must have the same timezones or'
    with pytest.raises(TypeError, match=msg):
        dti_tz - dti
    with pytest.raises(TypeError, match=msg):
        dti - dti_tz
    with pytest.raises(TypeError, match=msg):
        dti_tz - dti_tz2
    dti -= dti
    tm.assert_index_equal(dti, expected)
    dti1 = date_range('20130101', periods=3)
    dti2 = date_range('20130101', periods=4)
    msg = 'cannot add indices of unequal length'
    with pytest.raises(ValueError, match=msg):
        dti1 - dti2
    dti1 = DatetimeIndex(['2012-01-01', np.nan, '2012-01-03'])
    dti2 = DatetimeIndex(['2012-01-02', '2012-01-03', np.nan])
    expected = TimedeltaIndex(['1 days', np.nan, np.nan])
    result = dti2 - dti1
    tm.assert_index_equal(result, expected)