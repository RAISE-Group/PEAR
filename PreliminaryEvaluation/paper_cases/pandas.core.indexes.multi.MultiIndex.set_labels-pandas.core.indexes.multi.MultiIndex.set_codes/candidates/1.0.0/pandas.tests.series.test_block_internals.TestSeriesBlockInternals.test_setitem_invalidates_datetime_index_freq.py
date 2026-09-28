def test_setitem_invalidates_datetime_index_freq(self):
    dti = pd.date_range('20130101', periods=3, tz='US/Eastern')
    ts = dti[1]
    ser = pd.Series(dti)
    assert ser._values is not dti
    assert ser._values._data.base is not dti._data._data.base
    assert dti.freq == 'D'
    ser.iloc[1] = pd.NaT
    assert ser._values.freq is None
    assert ser._values is not dti
    assert ser._values._data.base is not dti._data._data.base
    assert dti[1] == ts
    assert dti.freq == 'D'