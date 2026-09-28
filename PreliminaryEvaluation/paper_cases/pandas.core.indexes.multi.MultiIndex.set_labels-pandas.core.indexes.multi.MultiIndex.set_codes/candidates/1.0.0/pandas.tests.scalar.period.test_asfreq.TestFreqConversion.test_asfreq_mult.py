def test_asfreq_mult(self):
    p = Period(freq='A', year=2007)
    for freq in ['3A', offsets.YearEnd(3)]:
        result = p.asfreq(freq)
        expected = Period('2007', freq='3A')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    for freq in ['3A', offsets.YearEnd(3)]:
        result = p.asfreq(freq, how='S')
        expected = Period('2007', freq='3A')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    p = Period(freq='3A', year=2007)
    for freq in ['A', offsets.YearEnd()]:
        result = p.asfreq(freq)
        expected = Period('2009', freq='A')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    for freq in ['A', offsets.YearEnd()]:
        result = p.asfreq(freq, how='S')
        expected = Period('2007', freq='A')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    p = Period(freq='A', year=2007)
    for freq in ['2M', offsets.MonthEnd(2)]:
        result = p.asfreq(freq)
        expected = Period('2007-12', freq='2M')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    for freq in ['2M', offsets.MonthEnd(2)]:
        result = p.asfreq(freq, how='S')
        expected = Period('2007-01', freq='2M')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    p = Period(freq='3A', year=2007)
    for freq in ['2M', offsets.MonthEnd(2)]:
        result = p.asfreq(freq)
        expected = Period('2009-12', freq='2M')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq
    for freq in ['2M', offsets.MonthEnd(2)]:
        result = p.asfreq(freq, how='S')
        expected = Period('2007-01', freq='2M')
        assert result == expected
        assert result.ordinal == expected.ordinal
        assert result.freq == expected.freq