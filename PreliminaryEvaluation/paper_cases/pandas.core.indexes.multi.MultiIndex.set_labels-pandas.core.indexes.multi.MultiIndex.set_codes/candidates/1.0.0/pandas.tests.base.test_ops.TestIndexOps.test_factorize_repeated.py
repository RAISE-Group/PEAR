def test_factorize_repeated(self):
    for orig in self.objs:
        o = orig.copy()
        if isinstance(o, Index) and o.is_boolean():
            continue
        if isinstance(o, Series):
            o = o.sort_values()
            n = o.iloc[5:].append(o)
        else:
            indexer = o.argsort()
            o = o.take(indexer)
            n = o[5:].append(o)
        exp_arr = np.array([5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.intp)
        codes, uniques = n.factorize(sort=True)
        tm.assert_numpy_array_equal(codes, exp_arr)
        if isinstance(o, Series):
            tm.assert_index_equal(uniques, Index(orig).sort_values(), check_names=False)
        else:
            tm.assert_index_equal(uniques, o, check_names=False)
        exp_arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4], np.intp)
        codes, uniques = n.factorize(sort=False)
        tm.assert_numpy_array_equal(codes, exp_arr)
        if isinstance(o, Series):
            expected = Index(o.iloc[5:10].append(o.iloc[:5]))
            tm.assert_index_equal(uniques, expected, check_names=False)
        else:
            expected = o[5:10].append(o[:5])
            tm.assert_index_equal(uniques, expected, check_names=False)