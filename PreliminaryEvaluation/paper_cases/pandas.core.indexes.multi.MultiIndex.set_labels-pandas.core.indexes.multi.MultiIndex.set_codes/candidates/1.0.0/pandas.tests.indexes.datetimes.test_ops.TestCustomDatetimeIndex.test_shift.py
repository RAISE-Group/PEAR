def test_shift(self):
    shifted = self.rng.shift(5)
    assert shifted[0] == self.rng[5]
    assert shifted.freq == self.rng.freq
    shifted = self.rng.shift(-5)
    assert shifted[5] == self.rng[0]
    assert shifted.freq == self.rng.freq
    shifted = self.rng.shift(0)
    assert shifted[0] == self.rng[0]
    assert shifted.freq == self.rng.freq
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', pd.errors.PerformanceWarning)
        rng = date_range(START, END, freq=BMonthEnd())
        shifted = rng.shift(1, freq=CDay())
        assert shifted[0] == rng[0] + CDay()