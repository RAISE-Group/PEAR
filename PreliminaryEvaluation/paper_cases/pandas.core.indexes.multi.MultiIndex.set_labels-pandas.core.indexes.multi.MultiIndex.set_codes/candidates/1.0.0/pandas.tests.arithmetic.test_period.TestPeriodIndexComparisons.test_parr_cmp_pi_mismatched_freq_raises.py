@pytest.mark.parametrize('freq', ['M', '2M', '3M'])
def test_parr_cmp_pi_mismatched_freq_raises(self, freq, box_with_array):
    base = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq=freq)
    base = tm.box_expected(base, box_with_array)
    msg = 'Input has different freq=A-DEC from '
    with pytest.raises(IncompatibleFrequency, match=msg):
        base <= Period('2011', freq='A')
    with pytest.raises(IncompatibleFrequency, match=msg):
        Period('2011', freq='A') >= base
    idx = PeriodIndex(['2011', '2012', '2013', '2014'], freq='A')
    rev_msg = 'Input has different freq=(M|2M|3M) from PeriodArray\\(freq=A-DEC\\)'
    idx_msg = rev_msg if box_with_array is tm.to_array else msg
    with pytest.raises(IncompatibleFrequency, match=idx_msg):
        base <= idx
    msg = 'Input has different freq=4M from '
    with pytest.raises(IncompatibleFrequency, match=msg):
        base <= Period('2011', freq='4M')
    with pytest.raises(IncompatibleFrequency, match=msg):
        Period('2011', freq='4M') >= base
    idx = PeriodIndex(['2011', '2012', '2013', '2014'], freq='4M')
    rev_msg = 'Input has different freq=(M|2M|3M) from PeriodArray\\(freq=4M\\)'
    idx_msg = rev_msg if box_with_array is tm.to_array else msg
    with pytest.raises(IncompatibleFrequency, match=idx_msg):
        base <= idx