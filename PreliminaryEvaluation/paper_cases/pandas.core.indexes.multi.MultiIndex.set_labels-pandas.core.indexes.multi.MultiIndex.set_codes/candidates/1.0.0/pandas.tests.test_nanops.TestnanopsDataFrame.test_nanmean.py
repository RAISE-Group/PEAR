def test_nanmean(self):
    self.check_funs(nanops.nanmean, np.mean, allow_complex=False, allow_obj=False, allow_date=False)