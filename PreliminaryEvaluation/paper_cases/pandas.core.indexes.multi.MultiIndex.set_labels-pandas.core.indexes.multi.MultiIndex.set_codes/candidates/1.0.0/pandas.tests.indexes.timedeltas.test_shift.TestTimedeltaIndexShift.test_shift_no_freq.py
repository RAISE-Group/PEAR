def test_shift_no_freq(self):
    tdi = TimedeltaIndex(['1 days 01:00:00', '2 days 01:00:00'], freq=None)
    with pytest.raises(NullFrequencyError):
        tdi.shift(2)