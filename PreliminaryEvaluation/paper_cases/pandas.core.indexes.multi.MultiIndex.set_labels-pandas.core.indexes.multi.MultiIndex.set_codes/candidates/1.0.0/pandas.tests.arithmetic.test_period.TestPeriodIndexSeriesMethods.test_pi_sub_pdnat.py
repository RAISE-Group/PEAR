def test_pi_sub_pdnat(self):
    idx = PeriodIndex(['2011-01', '2011-02', 'NaT', '2011-04'], freq='M', name='idx')
    exp = pd.TimedeltaIndex([pd.NaT] * 4, name='idx')
    tm.assert_index_equal(pd.NaT - idx, exp)
    tm.assert_index_equal(idx - pd.NaT, exp)