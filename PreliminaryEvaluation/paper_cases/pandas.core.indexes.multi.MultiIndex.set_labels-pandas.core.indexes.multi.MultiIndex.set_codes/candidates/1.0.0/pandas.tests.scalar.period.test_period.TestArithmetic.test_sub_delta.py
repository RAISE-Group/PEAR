def test_sub_delta(self):
    left, right = (Period('2011', freq='A'), Period('2007', freq='A'))
    result = left - right
    assert result == 4 * right.freq
    with pytest.raises(IncompatibleFrequency):
        left - Period('2007-01', freq='M')