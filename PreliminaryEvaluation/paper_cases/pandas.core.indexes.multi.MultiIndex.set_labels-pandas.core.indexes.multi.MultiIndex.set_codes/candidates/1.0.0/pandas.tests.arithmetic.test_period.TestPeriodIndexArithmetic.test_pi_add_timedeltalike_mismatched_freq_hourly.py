def test_pi_add_timedeltalike_mismatched_freq_hourly(self, not_hourly):
    other = not_hourly
    rng = pd.period_range('2014-01-01 10:00', '2014-01-05 10:00', freq='H')
    msg = 'Input has different freq(=.+)? from Period.*?\\(freq=H\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng + other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng += other