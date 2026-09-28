def test_is_period(self):
    assert lib.is_period(pd.Period('2011-01', freq='M'))
    assert not lib.is_period(pd.PeriodIndex(['2011-01'], freq='M'))
    assert not lib.is_period(pd.Timestamp('2011-01'))
    assert not lib.is_period(1)
    assert not lib.is_period(np.nan)