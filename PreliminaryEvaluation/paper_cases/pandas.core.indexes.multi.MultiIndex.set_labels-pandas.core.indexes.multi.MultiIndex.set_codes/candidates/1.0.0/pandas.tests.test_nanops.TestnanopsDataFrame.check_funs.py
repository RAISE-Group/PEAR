def check_funs(self, testfunc, targfunc, allow_complex=True, allow_all_nan=True, allow_date=True, allow_tdelta=True, allow_obj=True, **kwargs):
    self.check_fun(testfunc, targfunc, 'arr_float', **kwargs)
    self.check_fun(testfunc, targfunc, 'arr_float_nan', **kwargs)
    self.check_fun(testfunc, targfunc, 'arr_int', **kwargs)
    self.check_fun(testfunc, targfunc, 'arr_bool', **kwargs)
    objs = [self.arr_float.astype('O'), self.arr_int.astype('O'), self.arr_bool.astype('O')]
    if allow_all_nan:
        self.check_fun(testfunc, targfunc, 'arr_nan', **kwargs)
    if allow_complex:
        self.check_fun(testfunc, targfunc, 'arr_complex', **kwargs)
        self.check_fun(testfunc, targfunc, 'arr_complex_nan', **kwargs)
        if allow_all_nan:
            self.check_fun(testfunc, targfunc, 'arr_nan_nanj', **kwargs)
        objs += [self.arr_complex.astype('O')]
    if allow_date:
        targfunc(self.arr_date)
        self.check_fun(testfunc, targfunc, 'arr_date', **kwargs)
        objs += [self.arr_date.astype('O')]
    if allow_tdelta:
        try:
            targfunc(self.arr_tdelta)
        except TypeError:
            pass
        else:
            self.check_fun(testfunc, targfunc, 'arr_tdelta', **kwargs)
            objs += [self.arr_tdelta.astype('O')]
    if allow_obj:
        self.arr_obj = np.vstack(objs)
        if allow_obj == 'convert':
            targfunc = partial(self._badobj_wrap, func=targfunc, allow_complex=allow_complex)
        self.check_fun(testfunc, targfunc, 'arr_obj', **kwargs)