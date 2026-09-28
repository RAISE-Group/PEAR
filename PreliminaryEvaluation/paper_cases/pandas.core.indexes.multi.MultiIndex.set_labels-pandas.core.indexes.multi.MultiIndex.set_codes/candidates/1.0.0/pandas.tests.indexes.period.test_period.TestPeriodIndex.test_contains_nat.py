def test_contains_nat(self):
    idx = period_range('2007-01', freq='M', periods=10)
    assert pd.NaT not in idx
    assert None not in idx
    assert float('nan') not in idx
    assert np.nan not in idx
    idx = pd.PeriodIndex(['2011-01', 'NaT', '2011-02'], freq='M')
    assert pd.NaT in idx
    assert None in idx
    assert float('nan') in idx
    assert np.nan in idx