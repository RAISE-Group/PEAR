def test_constructor_infer_freq(self):
    p = Period('2007-01-01')
    assert p.freq == 'D'
    p = Period('2007-01-01 07')
    assert p.freq == 'H'
    p = Period('2007-01-01 07:10')
    assert p.freq == 'T'
    p = Period('2007-01-01 07:10:15')
    assert p.freq == 'S'
    p = Period('2007-01-01 07:10:15.123')
    assert p.freq == 'L'
    p = Period('2007-01-01 07:10:15.123000')
    assert p.freq == 'L'
    p = Period('2007-01-01 07:10:15.123400')
    assert p.freq == 'U'