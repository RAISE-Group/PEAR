def test_binops_pow(self):
    ops = [pow]
    scalars = [1, 2]
    idxs = [pd.RangeIndex(0, 10, 1), pd.RangeIndex(0, 20, 2)]
    self.check_binop(ops, scalars, idxs)