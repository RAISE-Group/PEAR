def test_contains(self):
    rng = period_range('2007-01', freq='M', periods=10)
    assert Period('2007-01', freq='M') in rng
    assert not Period('2007-01', freq='D') in rng
    assert not Period('2007-01', freq='2M') in rng