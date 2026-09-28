def test_nanargmax(self):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', RuntimeWarning)
        func = partial(self._argminmax_wrap, func=np.argmax)
        self.check_funs(nanops.nanargmax, func, allow_obj=False)