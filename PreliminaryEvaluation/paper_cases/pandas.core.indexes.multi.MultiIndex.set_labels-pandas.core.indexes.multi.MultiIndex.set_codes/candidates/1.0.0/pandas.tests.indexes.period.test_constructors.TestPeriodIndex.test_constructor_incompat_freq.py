def test_constructor_incompat_freq(self):
    msg = 'Input has different freq=D from PeriodIndex\\(freq=M\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        PeriodIndex([Period('2011-01', freq='M'), pd.NaT, Period('2011-01', freq='D')])
    with pytest.raises(IncompatibleFrequency, match=msg):
        PeriodIndex(np.array([Period('2011-01', freq='M'), pd.NaT, Period('2011-01', freq='D')]))
    with pytest.raises(IncompatibleFrequency, match=msg):
        PeriodIndex([pd.NaT, Period('2011-01', freq='M'), Period('2011-01', freq='D')])
    with pytest.raises(IncompatibleFrequency, match=msg):
        PeriodIndex(np.array([pd.NaT, Period('2011-01', freq='M'), Period('2011-01', freq='D')]))