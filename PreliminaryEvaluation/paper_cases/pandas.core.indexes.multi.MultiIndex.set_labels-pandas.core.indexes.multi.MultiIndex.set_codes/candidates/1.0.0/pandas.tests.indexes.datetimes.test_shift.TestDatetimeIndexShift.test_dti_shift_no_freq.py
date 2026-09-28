def test_dti_shift_no_freq(self):
    dti = pd.DatetimeIndex(['2011-01-01 10:00', '2011-01-01'], freq=None)
    with pytest.raises(NullFrequencyError):
        dti.shift(2)