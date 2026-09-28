def test_factorize(self):
    for orig in self.objs:
        o = orig.copy()
        if isinstance(o, Index) and o.is_boolean():
            exp_arr = np.array([0, 1] + [0] * 8, dtype=np.intp)
            exp_uniques = o
            exp_uniques = Index([False, True])
        else:
            exp_arr = np.array(range(len(o)), dtype=np.intp)
            exp_uniques = o
        codes, uniques = o.factorize()
        tm.assert_numpy_array_equal(codes, exp_arr)
        if isinstance(o, Series):
            tm.assert_index_equal(uniques, Index(orig), check_names=False)
        else:
            tm.assert_index_equal(uniques, exp_uniques, check_names=False)