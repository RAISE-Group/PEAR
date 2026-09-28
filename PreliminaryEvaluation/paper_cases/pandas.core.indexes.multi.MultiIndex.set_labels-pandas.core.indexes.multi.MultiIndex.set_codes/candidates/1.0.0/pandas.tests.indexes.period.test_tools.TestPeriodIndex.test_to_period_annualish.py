@pytest.mark.parametrize('off', ['BA', 'AS', 'BAS'])
def test_to_period_annualish(self, off):
    rng = date_range('01-Jan-2012', periods=8, freq=off)
    prng = rng.to_period()
    assert prng.freq == 'A-DEC'