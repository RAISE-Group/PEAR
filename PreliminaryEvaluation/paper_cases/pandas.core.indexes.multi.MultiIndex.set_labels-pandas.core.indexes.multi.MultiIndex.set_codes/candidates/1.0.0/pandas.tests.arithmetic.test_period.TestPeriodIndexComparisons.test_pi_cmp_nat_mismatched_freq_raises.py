@pytest.mark.parametrize('freq', ['M', '2M', '3M'])
def test_pi_cmp_nat_mismatched_freq_raises(self, freq):
    idx1 = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-05'], freq=freq)
    diff = PeriodIndex(['2011-02', '2011-01', '2011-04', 'NaT'], freq='4M')
    msg = 'Input has different freq=4M from Period(Array|Index)'
    with pytest.raises(IncompatibleFrequency, match=msg):
        idx1 > diff
    with pytest.raises(IncompatibleFrequency, match=msg):
        idx1 == diff