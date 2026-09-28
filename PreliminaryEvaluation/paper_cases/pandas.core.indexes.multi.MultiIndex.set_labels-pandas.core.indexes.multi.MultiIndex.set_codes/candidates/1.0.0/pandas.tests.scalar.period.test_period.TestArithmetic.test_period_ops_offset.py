def test_period_ops_offset(self):
    p = Period('2011-04-01', freq='D')
    result = p + offsets.Day()
    exp = Period('2011-04-02', freq='D')
    assert result == exp
    result = p - offsets.Day(2)
    exp = Period('2011-03-30', freq='D')
    assert result == exp
    msg = 'Input cannot be converted to Period\\(freq=D\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        p + offsets.Hour(2)
    with pytest.raises(IncompatibleFrequency, match=msg):
        p - offsets.Hour(2)