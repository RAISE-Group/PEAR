@td.skip_if_no_scipy
@pytest.mark.parametrize('ddof', range(3))
def test_nansem(self, ddof):
    from scipy.stats import sem
    with np.errstate(invalid='ignore'):
        self.check_funs(nanops.nansem, sem, allow_complex=False, allow_date=False, allow_tdelta=False, allow_obj='convert', ddof=ddof)