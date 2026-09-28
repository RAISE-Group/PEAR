def test_pi_add_sub_timedeltalike_freq_mismatch_annual(self, mismatched_freq):
    other = mismatched_freq
    rng = pd.period_range('2014', '2024', freq='A')
    msg = 'Input has different freq(=.+)? from Period.*?\\(freq=A-DEC\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng + other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng += other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng - other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng -= other