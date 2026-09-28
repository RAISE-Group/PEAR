def test_pi_cmp_period(self):
    idx = period_range('2007-01', periods=20, freq='M')
    result = idx < idx[10]
    exp = idx.values < idx.values[10]
    tm.assert_numpy_array_equal(result, exp)