def test_pi_sub_period_nat(self):
    idx = PeriodIndex(['2011-01', 'NaT', '2011-03', '2011-04'], freq='M', name='idx')
    result = idx - pd.Period('2012-01', freq='M')
    off = idx.freq
    exp = pd.Index([-12 * off, pd.NaT, -10 * off, -9 * off], name='idx')
    tm.assert_index_equal(result, exp)
    result = pd.Period('2012-01', freq='M') - idx
    exp = pd.Index([12 * off, pd.NaT, 10 * off, 9 * off], name='idx')
    tm.assert_index_equal(result, exp)
    exp = pd.TimedeltaIndex([np.nan, np.nan, np.nan, np.nan], name='idx')
    tm.assert_index_equal(idx - pd.Period('NaT', freq='M'), exp)
    tm.assert_index_equal(pd.Period('NaT', freq='M') - idx, exp)