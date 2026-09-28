def test_construction_bday(self):
    i1 = Period('3/10/12', freq='B')
    i2 = Period('3/10/12', freq='D')
    assert i1 == i2.asfreq('B')
    i2 = Period('3/11/12', freq='D')
    assert i1 == i2.asfreq('B')
    i2 = Period('3/12/12', freq='D')
    assert i1 == i2.asfreq('B')
    i3 = Period('3/10/12', freq='b')
    assert i1 == i3
    i1 = Period(year=2012, month=3, day=10, freq='B')
    i2 = Period('3/12/12', freq='B')
    assert i1 == i2