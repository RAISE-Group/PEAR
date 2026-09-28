def test_freq_str(self):
    i1 = Period('1982', freq='Min')
    assert i1.freq == offsets.Minute()
    assert i1.freqstr == 'T'