def test_dt64tz_setitem_does_not_mutate_dti(self):
    dti = pd.date_range('2016-01-01', periods=10, tz='US/Pacific')
    ts = dti[0]
    ser = pd.Series(dti)
    assert ser._values is not dti
    assert ser._values._data.base is not dti._data._data.base
    assert ser._data.blocks[0].values is not dti
    assert ser._data.blocks[0].values._data.base is not dti._data._data.base
    ser[::3] = pd.NaT
    assert ser[0] is pd.NaT
    assert dti[0] == ts