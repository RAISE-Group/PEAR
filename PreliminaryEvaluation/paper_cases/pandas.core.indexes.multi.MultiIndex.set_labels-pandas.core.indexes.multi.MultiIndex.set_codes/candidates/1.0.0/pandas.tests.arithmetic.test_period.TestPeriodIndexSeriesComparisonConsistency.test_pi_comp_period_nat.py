def test_pi_comp_period_nat(self):
    idx = PeriodIndex(['2011-01', 'NaT', '2011-03', '2011-04'], freq='M', name='idx')
    f = lambda x: x == pd.Period('2011-03', freq='M')
    exp = np.array([False, False, True, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') == x
    self._check(idx, f, exp)
    f = lambda x: x == pd.NaT
    exp = np.array([False, False, False, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.NaT == x
    self._check(idx, f, exp)
    f = lambda x: x != pd.Period('2011-03', freq='M')
    exp = np.array([True, True, False, True], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') != x
    self._check(idx, f, exp)
    f = lambda x: x != pd.NaT
    exp = np.array([True, True, True, True], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.NaT != x
    self._check(idx, f, exp)
    f = lambda x: pd.Period('2011-03', freq='M') >= x
    exp = np.array([True, False, True, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: x < pd.Period('2011-03', freq='M')
    exp = np.array([True, False, False, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: x > pd.NaT
    exp = np.array([False, False, False, False], dtype=np.bool)
    self._check(idx, f, exp)
    f = lambda x: pd.NaT >= x
    exp = np.array([False, False, False, False], dtype=np.bool)
    self._check(idx, f, exp)