@pytest.mark.parametrize('ddof', range(3))
def test_nanvar(self, ddof):
    self.check_funs(nanops.nanvar, np.var, allow_complex=False, allow_date=False, allow_obj='convert', ddof=ddof)