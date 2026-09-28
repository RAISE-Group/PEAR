def test_constructor_use_start_freq(self):
    p = Period('4/2/2012', freq='B')
    expected = period_range(start='4/2/2012', periods=10, freq='B')
    index = period_range(start=p, periods=10)
    tm.assert_index_equal(index, expected)