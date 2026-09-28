def check_fun_data(self, testfunc, targfunc, testarval, targarval, check_dtype=True, empty_targfunc=None, **kwargs):
    for axis in list(range(targarval.ndim)) + [None]:
        for skipna in [False, True]:
            targartempval = targarval if skipna else testarval
            if skipna and empty_targfunc and isna(targartempval).all():
                targ = empty_targfunc(targartempval, axis=axis, **kwargs)
            else:
                targ = targfunc(targartempval, axis=axis, **kwargs)
            res = testfunc(testarval, axis=axis, skipna=skipna, **kwargs)
            self.check_results(targ, res, axis, check_dtype=check_dtype)
            if skipna:
                res = testfunc(testarval, axis=axis, **kwargs)
                self.check_results(targ, res, axis, check_dtype=check_dtype)
            if axis is None:
                res = testfunc(testarval, skipna=skipna, **kwargs)
                self.check_results(targ, res, axis, check_dtype=check_dtype)
            if skipna and axis is None:
                res = testfunc(testarval, **kwargs)
                self.check_results(targ, res, axis, check_dtype=check_dtype)
    if testarval.ndim <= 1:
        return
    testarval2 = np.take(testarval, 0, axis=-1)
    targarval2 = np.take(targarval, 0, axis=-1)
    self.check_fun_data(testfunc, targfunc, testarval2, targarval2, check_dtype=check_dtype, empty_targfunc=empty_targfunc, **kwargs)