@pytest.mark.parametrize('freq', ['A', 'M', 'D', 'T', 'S'])
@pytest.mark.parametrize('mult', [1, 2, 3, 4, 5])
def test_constructor_freq_mult_dti_compat(self, mult, freq):
    freqstr = str(mult) + freq
    pidx = period_range(start='2014-04-01', freq=freqstr, periods=10)
    expected = date_range(start='2014-04-01', freq=freqstr, periods=10).to_period(freqstr)
    tm.assert_index_equal(pidx, expected)