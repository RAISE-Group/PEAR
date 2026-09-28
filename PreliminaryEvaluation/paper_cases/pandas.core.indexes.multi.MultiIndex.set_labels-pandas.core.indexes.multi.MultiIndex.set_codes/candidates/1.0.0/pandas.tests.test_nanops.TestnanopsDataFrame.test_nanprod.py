def test_nanprod(self):
    self.check_funs(nanops.nanprod, np.prod, allow_date=False, allow_tdelta=False, empty_targfunc=np.nanprod)