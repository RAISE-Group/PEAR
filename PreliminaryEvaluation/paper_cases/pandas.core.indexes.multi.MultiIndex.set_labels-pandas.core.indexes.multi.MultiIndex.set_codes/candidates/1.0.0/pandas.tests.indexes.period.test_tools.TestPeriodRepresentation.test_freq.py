@pytest.mark.parametrize('freq', ['W-THU', 'D', 'B', 'H', 'T', 'S', 'L', 'U', 'N'])
def test_freq(self, freq):
    self._check_freq(freq, '1970-01-01')