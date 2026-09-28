def check_nancomp(self, checkfun, targ0):
    arr_float = self.arr_float
    arr_float1 = self.arr_float1
    arr_nan = self.arr_nan
    arr_nan_nan = self.arr_nan_nan
    arr_float_nan = self.arr_float_nan
    arr_float1_nan = self.arr_float1_nan
    arr_nan_float1 = self.arr_nan_float1
    while targ0.ndim:
        res0 = checkfun(arr_float, arr_float1)
        tm.assert_almost_equal(targ0, res0)
        if targ0.ndim > 1:
            targ1 = np.vstack([targ0, arr_nan])
        else:
            targ1 = np.hstack([targ0, arr_nan])
        res1 = checkfun(arr_float_nan, arr_float1_nan)
        tm.assert_numpy_array_equal(targ1, res1, check_dtype=False)
        targ2 = arr_nan_nan
        res2 = checkfun(arr_float_nan, arr_nan_float1)
        tm.assert_numpy_array_equal(targ2, res2, check_dtype=False)
        arr_float = np.take(arr_float, 0, axis=-1)
        arr_float1 = np.take(arr_float1, 0, axis=-1)
        arr_nan = np.take(arr_nan, 0, axis=-1)
        arr_nan_nan = np.take(arr_nan_nan, 0, axis=-1)
        arr_float_nan = np.take(arr_float_nan, 0, axis=-1)
        arr_float1_nan = np.take(arr_float1_nan, 0, axis=-1)
        arr_nan_float1 = np.take(arr_nan_float1, 0, axis=-1)
        targ0 = np.take(targ0, 0, axis=-1)