def test_pi_comp_period(self):
    idx = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq='M', name='idx')
    f = lambda x: x == pd.Period('2011-03', freq='M')
    exp = np.array([False, False, True, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') == x
    self._check(idx, f, exp)
    f = lambda x: x != pd.Period('2011-03', freq='M')
    exp = np.array([True, True, False, True], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') != x
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') >= x
    exp = np.array([True, True, True, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: x > pd.Period('2011-03', freq='M')
    exp = np.array([False, False, False, True], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') >= x
    exp = np.array([True, True, True, False], dtype=np.bool)
    self._check(idx, f, exp)