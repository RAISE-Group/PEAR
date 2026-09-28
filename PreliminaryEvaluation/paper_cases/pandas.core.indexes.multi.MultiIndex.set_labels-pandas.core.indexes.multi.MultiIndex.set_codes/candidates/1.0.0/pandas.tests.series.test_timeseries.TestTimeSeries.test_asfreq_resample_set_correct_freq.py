def test_asfreq_resample_set_correct_freq(self):
    df = pd.DataFrame({'date': ['2012-01-01', '2012-01-02', '2012-01-03'], 'col': [1, 2, 3]})
    df = df.set_index(pd.to_datetime(df.date))
    assert df.index.freq is None
    assert df.index.inferred_freq == 'D'
    assert df.asfreq('D').index.freq == 'D'
    assert df.resample('D').asfreq().index.freq == 'D'