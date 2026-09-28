def test_construction(self):
    i1 = Period('1/1/2005', freq='M')
    i2 = Period('Jan 2005')
    assert i1 == i2
    i1 = Period('2005', freq='A')
    i2 = Period('2005')
    i3 = Period('2005', freq='a')
    assert i1 == i2
    assert i1 == i3
    i4 = Period('2005', freq='M')
    i5 = Period('2005', freq='m')
    msg = 'Input has different freq=M from Period\\(freq=A-DEC\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        i1 != i4
    assert i4 == i5
    i1 = Period.now('Q')
    i2 = Period(datetime.now(), freq='Q')
    i3 = Period.now('q')
    assert i1 == i2
    assert i1 == i3
    i1 = Period('1982', freq='min')
    i2 = Period('1982', freq='MIN')
    assert i1 == i2
    i2 = Period('1982', freq=('Min', 1))
    assert i1 == i2
    i1 = Period(year=2005, month=3, day=1, freq='D')
    i2 = Period('3/1/2005', freq='D')
    assert i1 == i2
    i3 = Period(year=2005, month=3, day=1, freq='d')
    assert i1 == i3
    i1 = Period('2007-01-01 09:00:00.001')
    expected = Period(datetime(2007, 1, 1, 9, 0, 0, 1000), freq='L')
    assert i1 == expected
    expected = Period(np_datetime64_compat('2007-01-01 09:00:00.001Z'), freq='L')
    assert i1 == expected
    i1 = Period('2007-01-01 09:00:00.00101')
    expected = Period(datetime(2007, 1, 1, 9, 0, 0, 1010), freq='U')
    assert i1 == expected
    expected = Period(np_datetime64_compat('2007-01-01 09:00:00.00101Z'), freq='U')
    assert i1 == expected
    msg = 'Must supply freq for ordinal value'
    with pytest.raises(ValueError, match=msg):
        Period(ordinal=200701)
    with pytest.raises(ValueError, match='Invalid frequency: X'):
        Period('2007-1-1', freq='X')