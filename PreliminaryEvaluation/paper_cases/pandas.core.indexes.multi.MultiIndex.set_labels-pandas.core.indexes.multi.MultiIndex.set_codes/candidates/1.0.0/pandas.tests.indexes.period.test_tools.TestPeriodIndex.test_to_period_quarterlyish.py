@pytest.mark.parametrize('off', ['BQ', 'QS', 'BQS'])
def test_to_period_quarterlyish(self, off):
    rng = date_range('01-Jan-2012', periods=8, freq=off)
    prng = rng.to_period()
    assert prng.freq == 'Q-DEC'