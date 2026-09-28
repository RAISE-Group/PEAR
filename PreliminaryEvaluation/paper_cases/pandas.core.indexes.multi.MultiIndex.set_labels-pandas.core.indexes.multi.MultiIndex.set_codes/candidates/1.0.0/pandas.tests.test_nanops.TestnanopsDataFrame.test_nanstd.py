@pytest.mark.parametrize('ddof', range(3))
def test_nanstd(self, ddof):
    self.check_funs(nanops.nanstd, np.std, allow_complex=False, allow_date=False, allow_obj='convert', ddof=ddof)