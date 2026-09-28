def test_nanargmin(self):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', RuntimeWarning)
        func = partial(self._argminmax_wrap, func=np.argmin)
        self.check_funs(nanops.nanargmin, func, allow_obj=False)