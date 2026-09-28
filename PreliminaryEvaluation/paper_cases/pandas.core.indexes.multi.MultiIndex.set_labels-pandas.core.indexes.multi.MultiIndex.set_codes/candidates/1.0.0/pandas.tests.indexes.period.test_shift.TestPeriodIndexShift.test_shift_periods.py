def test_shift_periods(self):
    idx = period_range(freq='A', start='1/1/2001', end='12/1/2009')
    tm.assert_index_equal(idx.shift(periods=0), idx)
    tm.assert_index_equal(idx.shift(0), idx)