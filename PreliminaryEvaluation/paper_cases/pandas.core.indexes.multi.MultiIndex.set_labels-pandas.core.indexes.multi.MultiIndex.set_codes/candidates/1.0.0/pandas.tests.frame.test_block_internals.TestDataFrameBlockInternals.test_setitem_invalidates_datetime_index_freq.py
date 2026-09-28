def test_setitem_invalidates_datetime_index_freq(self):
    dti = date_range('20130101', periods=3, tz='US/Eastern')
    ts = dti[1]
    df = DataFrame({'B': dti})
    assert df['B']._values.freq == 'D'
    df.iloc[1, 0] = pd.NaT
    assert df['B']._values.freq is None
    assert dti.freq == 'D'
    assert dti[1] == ts