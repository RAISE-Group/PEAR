def check_binop(self, ops, scalars, idxs):
    for op in ops:
        for a, b in combinations(idxs, 2):
            result = op(a, b)
            expected = op(pd.Int64Index(a), pd.Int64Index(b))
            tm.assert_index_equal(result, expected)
        for idx in idxs:
            for scalar in scalars:
                result = op(idx, scalar)
                expected = op(pd.Int64Index(idx), scalar)
                tm.assert_index_equal(result, expected)