def test_asfreq_combined(self):
    p = Period('2007', freq='H')
    expected = Period('2007', freq='25H')
    for freq, how in zip(['1D1H', '1H1D'], ['E', 'S']):
        result = p.asfreq(freq, how=how)
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    p1 = Period(freq='1D1H', year=2007)
    p2 = Period(freq='1H1D', year=2007)
    result1 = p1.asfreq('H')
    result2 = p2.asfreq('H')
    expected = Period('2007-01-02', freq='H')
    assert result1 == expected
    assert result1.ordinal == expected.ordinal
    assert result1.freq == expected.freq
    assert result2 == expected
    assert result2.ordinal == expected.ordinal
    assert result2.freq == expected.freq
    result1 = p1.asfreq('H', how='S')
    result2 = p2.asfreq('H', how='S')
    expected = Period('2007-01-01', freq='H')
    assert result1 == expected
    assert result1.ordinal == expected.ordinal
    assert result1.freq == expected.freq
    assert result2 == expected
    assert result2.ordinal == expected.ordinal
    assert result2.freq == expected.freq