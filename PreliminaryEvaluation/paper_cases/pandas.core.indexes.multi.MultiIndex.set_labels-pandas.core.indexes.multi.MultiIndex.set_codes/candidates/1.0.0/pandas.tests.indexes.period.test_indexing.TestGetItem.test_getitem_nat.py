def test_getitem_nat(self):
    idx = pd.PeriodIndex(['2011-01', 'NaT', '2011-02'], freq='M')
    assert idx[0] == pd.Period('2011-01', freq='M')
    assert idx[1] is pd.NaT
    s = pd.Series([0, 1, 2], index=idx)
    assert s[pd.NaT] == 1
    s = pd.Series(idx, index=idx)
    assert s[pd.Period('2011-01', freq='M')] == pd.Period('2011-01', freq='M')
    assert s[pd.NaT] is pd.NaT