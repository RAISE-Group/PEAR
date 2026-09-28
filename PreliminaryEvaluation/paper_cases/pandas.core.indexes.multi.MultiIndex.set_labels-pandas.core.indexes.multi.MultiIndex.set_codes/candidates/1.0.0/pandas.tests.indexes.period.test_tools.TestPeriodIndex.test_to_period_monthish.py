def test_to_period_monthish(self):
    offsets = ['MS', 'BM']
    for off in offsets:
        rng = date_range('01-Jan-2012', periods=8, freq=off)
        prng = rng.to_period()
        assert prng.freq == 'M'
    rng = date_range('01-Jan-2012', periods=8, freq='M')
    prng = rng.to_period()
    assert prng.freq == 'M'
    msg = pd._libs.tslibs.frequencies.INVALID_FREQ_ERR_MSG
    with pytest.raises(ValueError, match=msg):
        date_range('01-Jan-2012', periods=8, freq='EOM')