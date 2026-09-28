def test_dti_constructor_preserve_dti_freq(self):
    rng = date_range('1/1/2000', '1/2/2000', freq='5min')
    rng2 = DatetimeIndex(rng)
    assert rng.freq == rng2.freq