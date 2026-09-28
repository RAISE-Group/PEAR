def test_binops(self):
    ops = [operator.add, operator.sub, operator.mul, operator.floordiv, operator.truediv]
    scalars = [-1, 1, 2]
    idxs = [pd.RangeIndex(0, 10, 1), pd.RangeIndex(0, 20, 2), pd.RangeIndex(-10, 10, 2), pd.RangeIndex(5, -5, -1)]
    self.check_binop(ops, scalars, idxs)