def test_pi_add_sub_timedeltalike_freq_mismatch_monthly(self, mismatched_freq):
    other = mismatched_freq
    rng = pd.period_range('2014-01', '2016-12', freq='M')
    msg = 'Input has different freq(=.+)? from Period.*?\\(freq=M\\)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng + other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng += other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng - other
    with pytest.raises(IncompatibleFrequency, match=msg):
        rng -= other