def test_shallow_copy_i8(self):
    pi = period_range('2018-01-01', periods=3, freq='2D')
    result = pi._shallow_copy(pi.asi8, freq=pi.freq)
    tm.assert_index_equal(result, pi)