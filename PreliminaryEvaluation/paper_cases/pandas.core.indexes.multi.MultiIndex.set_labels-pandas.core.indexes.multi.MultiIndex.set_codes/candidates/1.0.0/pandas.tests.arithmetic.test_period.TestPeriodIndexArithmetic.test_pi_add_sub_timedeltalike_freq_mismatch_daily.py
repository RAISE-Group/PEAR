def test_pi_add_sub_timedeltalike_freq_mismatch_daily(self, not_daily):
    other = not_daily
    rng = pd.period_range('2014-05-01', '2014-05-15', freq='D')
    msg = 'Input has different freq(=.+)? from Period.*?\\(freq=D\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng + other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng += other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng - other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng -= other