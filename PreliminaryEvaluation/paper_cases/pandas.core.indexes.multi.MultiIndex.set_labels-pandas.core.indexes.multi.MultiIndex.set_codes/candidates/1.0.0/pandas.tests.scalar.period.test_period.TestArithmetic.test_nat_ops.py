@pytest.mark.parametrize('freq', ['M', '2M', '3M'])
def test_nat_ops(self, freq):
    p = Period('NaT', freq=freq)
    assert p is NaT
    assert p + 1 is NaT
    assert 1 + p is NaT
    assert p - 1 is NaT
    assert p - Period('2011-01', freq=freq) is NaT
    assert Period('2011-01', freq=freq) - p is NaT