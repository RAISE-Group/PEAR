@td.skip_if_no_scipy
def test_nanskew(self):
    from scipy.stats import skew
    func = partial(self._skew_kurt_wrap, func=skew)
    with np.errstate(invalid='ignore'):
        self.check_funs(nanops.nanskew, func, allow_complex=False, allow_date=False, allow_tdelta=False)