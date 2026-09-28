def test_repr_nat(self):
    p = Period('nat', freq='M')
    assert repr(NaT) in repr(p)