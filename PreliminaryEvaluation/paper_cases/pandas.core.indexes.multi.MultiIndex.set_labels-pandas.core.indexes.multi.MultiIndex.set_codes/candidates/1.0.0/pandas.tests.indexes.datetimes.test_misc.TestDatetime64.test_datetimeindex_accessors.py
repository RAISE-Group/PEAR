def test_datetimeindex_accessors(self):
    dti_naive = pd.date_range(freq='D', start=datetime(1998, 1, 1), periods=365)
    dti_tz = pd.date_range(freq='D', start=datetime(1998, 1, 1), periods=365, tz='US/Eastern')
    for dti in [dti_naive, dti_tz]:
        assert dti.year[0] == 1998
        assert dti.month[0] == 1
        assert dti.day[0] == 1
        assert dti.hour[0] == 0
        assert dti.minute[0] == 0
        assert dti.second[0] == 0
        assert dti.microsecond[0] == 0
        assert dti.dayofweek[0] == 3
        assert dti.dayofyear[0] == 1
        assert dti.dayofyear[120] == 121
        assert dti.weekofyear[0] == 1
        assert dti.weekofyear[120] == 18
        assert dti.quarter[0] == 1
        assert dti.quarter[120] == 2
        assert dti.days_in_month[0] == 31
        assert dti.days_in_month[90] == 30
        assert dti.is_month_start[0]
        assert not dti.is_month_start[1]
        assert dti.is_month_start[31]
        assert dti.is_quarter_start[0]
        assert dti.is_quarter_start[90]
        assert dti.is_year_start[0]
        assert not dti.is_year_start[364]
        assert not dti.is_month_end[0]
        assert dti.is_month_end[30]
        assert not dti.is_month_end[31]
        assert dti.is_month_end[364]
        assert not dti.is_quarter_end[0]
        assert not dti.is_quarter_end[30]
        assert dti.is_quarter_end[89]
        assert dti.is_quarter_end[364]
        assert not dti.is_year_end[0]
        assert dti.is_year_end[364]
        assert len(dti.year) == 365
        assert len(dti.month) == 365
        assert len(dti.day) == 365
        assert len(dti.hour) == 365
        assert len(dti.minute) == 365
        assert len(dti.second) == 365
        assert len(dti.microsecond) == 365
        assert len(dti.dayofweek) == 365
        assert len(dti.dayofyear) == 365
        assert len(dti.weekofyear) == 365
        assert len(dti.quarter) == 365
        assert len(dti.is_month_start) == 365
        assert len(dti.is_month_end) == 365
        assert len(dti.is_quarter_start) == 365
        assert len(dti.is_quarter_end) == 365
        assert len(dti.is_year_start) == 365
        assert len(dti.is_year_end) == 365
        dti.name = 'name'
        for accessor in DatetimeIndex._field_ops:
            res = getattr(dti, accessor)
            assert len(res) == 365
            assert isinstance(res, Index)
            assert res.name == 'name'
        for accessor in DatetimeIndex._bool_ops:
            res = getattr(dti, accessor)
            assert len(res) == 365
            assert isinstance(res, np.ndarray)
        res = dti[dti.is_quarter_start]
        exp = dti[[0, 90, 181, 273]]
        tm.assert_index_equal(res, exp)
        res = dti[dti.is_leap_year]
        exp = DatetimeIndex([], freq='D', tz=dti.tz, name='name')
        tm.assert_index_equal(res, exp)
    dti = pd.date_range(freq='BQ-FEB', start=datetime(1998, 1, 1), periods=4)
    assert sum(dti.is_quarter_start) == 0
    assert sum(dti.is_quarter_end) == 4
    assert sum(dti.is_year_start) == 0
    assert sum(dti.is_year_end) == 1
    bday_egypt = offsets.CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')
    dti = date_range(datetime(2013, 4, 30), periods=5, freq=bday_egypt)
    msg = 'Custom business days is not supported by is_month_start'
    with pytest.raises(ValueError, match=msg):
        dti.is_month_start
    dti = DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03'])
    assert dti.is_month_start[0] == 1
    tests = [(Timestamp('2013-06-01', freq='M').is_month_start, 1), (Timestamp('2013-06-01', freq='BM').is_month_start, 0), (Timestamp('2013-06-03', freq='M').is_month_start, 0), (Timestamp('2013-06-03', freq='BM').is_month_start, 1), (Timestamp('2013-02-28', freq='Q-FEB').is_month_end, 1), (Timestamp('2013-02-28', freq='Q-FEB').is_quarter_end, 1), (Timestamp('2013-02-28', freq='Q-FEB').is_year_end, 1), (Timestamp('2013-03-01', freq='Q-FEB').is_month_start, 1), (Timestamp('2013-03-01', freq='Q-FEB').is_quarter_start, 1), (Timestamp('2013-03-01', freq='Q-FEB').is_year_start, 1), (Timestamp('2013-03-31', freq='QS-FEB').is_month_end, 1), (Timestamp('2013-03-31', freq='QS-FEB').is_quarter_end, 0), (Timestamp('2013-03-31', freq='QS-FEB').is_year_end, 0), (Timestamp('2013-02-01', freq='QS-FEB').is_month_start, 1), (Timestamp('2013-02-01', freq='QS-FEB').is_quarter_start, 1), (Timestamp('2013-02-01', freq='QS-FEB').is_year_start, 1), (Timestamp('2013-06-30', freq='BQ').is_month_end, 0), (Timestamp('2013-06-30', freq='BQ').is_quarter_end, 0), (Timestamp('2013-06-30', freq='BQ').is_year_end, 0), (Timestamp('2013-06-28', freq='BQ').is_month_end, 1), (Timestamp('2013-06-28', freq='BQ').is_quarter_end, 1), (Timestamp('2013-06-28', freq='BQ').is_year_end, 0), (Timestamp('2013-06-30', freq='BQS-APR').is_month_end, 0), (Timestamp('2013-06-30', freq='BQS-APR').is_quarter_end, 0), (Timestamp('2013-06-30', freq='BQS-APR').is_year_end, 0), (Timestamp('2013-06-28', freq='BQS-APR').is_month_end, 1), (Timestamp('2013-06-28', freq='BQS-APR').is_quarter_end, 1), (Timestamp('2013-03-29', freq='BQS-APR').is_year_end, 1), (Timestamp('2013-11-01', freq='AS-NOV').is_year_start, 1), (Timestamp('2013-10-31', freq='AS-NOV').is_year_end, 1), (Timestamp('2012-02-01').days_in_month, 29), (Timestamp('2013-02-01').days_in_month, 28)]
    for ts, value in tests:
        assert ts == value
    dates = ['2013/12/29', '2013/12/30', '2013/12/31']
    dates = DatetimeIndex(dates, tz='Europe/Brussels')
    expected = [52, 1, 1]
    assert dates.weekofyear.tolist() == expected
    assert [d.weekofyear for d in dates] == expected