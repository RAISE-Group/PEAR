def test_ncols(self):
    test_sers = gen_series_formatting()
    for s in test_sers.values():
        self.chck_ncols(s)