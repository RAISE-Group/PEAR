def test_minmax_period(self):
    idx1 = pd.PeriodIndex([NaT, '2011-01-01', '2011-01-02', '2011-01-03'], freq='D')
    assert idx1.is_monotonic
    idx2 = pd.PeriodIndex(['2011-01-01', NaT, '2011-01-03', '2011-01-02', NaT], freq='D')
    assert not idx2.is_monotonic
    for idx in [idx1, idx2]:
        assert idx.min() == pd.Period('2011-01-01', freq='D')
        assert idx.max() == pd.Period('2011-01-03', freq='D')
    assert idx1.argmin() == 1
    assert idx2.argmin() == 0
    assert idx1.argmax() == 3
    assert idx2.argmax() == 2
    for op in ['min', 'max']:
        obj = PeriodIndex([], freq='M')
        result = getattr(obj, op)()
        assert result is NaT
        obj = PeriodIndex([NaT], freq='M')
        result = getattr(obj, op)()
        assert result is NaT
        obj = PeriodIndex([NaT, NaT, NaT], freq='M')
        result = getattr(obj, op)()
        assert result is NaT