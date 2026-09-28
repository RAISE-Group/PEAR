def test_nanmedian(self):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', RuntimeWarning)
        self.check_funs(nanops.nanmedian, np.median, allow_complex=False, allow_date=False, allow_obj='convert')