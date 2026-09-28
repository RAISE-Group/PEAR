def test_timedelta64_nan(self):
    td = Series([timedelta(days=i) for i in range(10)])
    td1 = td.copy()
    td1[0] = np.nan
    assert isna(td1[0])
    assert td1[0].value == iNaT
    td1[0] = td[0]
    assert not isna(td1[0])
    td1[1] = iNaT
    assert not isna(td1[1])
    assert td1.dtype == np.object_
    assert td1[1] == iNaT
    td1[1] = td[1]
    assert not isna(td1[1])
    td1[2] = NaT
    assert isna(td1[2])
    assert td1[2].value == iNaT
    td1[2] = td[2]
    assert not isna(td1[2])