def test_resample_bms_2752(self):
    foo = Series(index=pd.bdate_range('20000101', '20000201'), dtype=np.float64)
    res1 = foo.resample('BMS').mean()
    res2 = foo.resample('BMS').mean().resample('B').mean()
    assert res1.index[0] == Timestamp('20000103')
    assert res1.index[0] == res2.index[0]