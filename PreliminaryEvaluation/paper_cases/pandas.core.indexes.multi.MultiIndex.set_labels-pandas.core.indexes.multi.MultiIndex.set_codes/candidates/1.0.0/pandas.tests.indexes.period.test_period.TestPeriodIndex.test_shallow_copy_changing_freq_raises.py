def test_shallow_copy_changing_freq_raises(self):
    pi = period_range('2018-01-01', periods=3, freq='2D')
    msg = 'specified freq and dtype are different'
    with pytest.raises(IncompatibleFrequency, match=msg):
        pi._shallow_copy(pi, freq='H')