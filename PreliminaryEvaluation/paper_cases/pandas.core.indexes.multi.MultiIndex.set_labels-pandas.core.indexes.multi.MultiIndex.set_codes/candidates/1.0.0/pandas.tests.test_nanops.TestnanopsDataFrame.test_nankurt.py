@td.skip_if_no_scipy
def test_nankurt(self):
    from scipy.stats import kurtosis
    func1 = partial(kurtosis, fisher=True)
    func = partial(self._skew_kurt_wrap, func=func1)
    with np.errstate(invalid='ignore'):
        self.check_funs(nanops.nankurt, func, allow_complex=False, allow_date=False, allow_tdelta=False)