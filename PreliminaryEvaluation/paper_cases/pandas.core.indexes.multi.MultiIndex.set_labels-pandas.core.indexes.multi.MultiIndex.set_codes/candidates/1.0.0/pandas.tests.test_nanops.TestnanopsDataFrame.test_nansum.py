def test_nansum(self):
    self.check_funs(nanops.nansum, np.sum, allow_date=False, check_dtype=False, empty_targfunc=np.nansum)