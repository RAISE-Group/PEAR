def test_add_sub_nat(self):
    p = Period('2011-01', freq='M')
    assert p + NaT is NaT
    assert NaT + p is NaT
    assert p - NaT is NaT
    assert NaT - p is NaT
    p = Period('NaT', freq='M')
    assert p is NaT
    assert p + NaT is NaT
    assert NaT + p is NaT
    assert p - NaT is NaT
    assert NaT - p is NaT