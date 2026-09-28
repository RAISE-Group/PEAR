def test_all_values_single_bin(self):
    index = period_range(start='2012-01-01', end='2012-12-31', freq='M')
    s = Series(np.random.randn(len(index)), index=index)
    result = s.resample('A').mean()
    tm.assert_almost_equal(result[0], s.mean())