def check_chained_cmp_op(self, lhs, cmp1, mid, cmp2, rhs):
    ex1 = f'lhs {cmp1} mid {cmp2} rhs'
    with pytest.raises(NotImplementedError):
        pd.eval(ex1, engine=self.engine, parser=self.parser)