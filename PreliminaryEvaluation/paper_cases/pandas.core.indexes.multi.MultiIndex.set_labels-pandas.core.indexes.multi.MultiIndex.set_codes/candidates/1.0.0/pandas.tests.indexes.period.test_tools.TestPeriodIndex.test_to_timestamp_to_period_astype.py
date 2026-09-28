def test_to_timestamp_to_period_astype(self):
    idx = DatetimeIndex([pd.NaT, '2011-01-01', '2011-02-01'], name='idx')
    res = idx.astype('period[M]')
    exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='M', name='idx')
    tm.assert_index_equal(res, exp)
    res = idx.astype('period[3M]')
    exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='3M', name='idx')
    tm.assert_index_equal(res, exp)