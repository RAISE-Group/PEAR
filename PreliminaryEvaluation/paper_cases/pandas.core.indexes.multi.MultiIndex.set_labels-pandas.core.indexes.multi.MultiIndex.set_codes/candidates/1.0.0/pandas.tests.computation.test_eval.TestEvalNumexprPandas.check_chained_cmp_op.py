def check_chained_cmp_op(self, lhs, cmp1, mid, cmp2, rhs):

    def check_operands(left, right, cmp_op):
        return _eval_single_bin(left, cmp_op, right, self.engine)
    lhs_new = check_operands(lhs, mid, cmp1)
    rhs_new = check_operands(mid, rhs, cmp2)
    if lhs_new is not None and rhs_new is not None:
        ex1 = f'lhs {cmp1} mid {cmp2} rhs'
        ex2 = f'lhs {cmp1} mid and mid {cmp2} rhs'
        ex3 = f'(lhs {cmp1} mid) & (mid {cmp2} rhs)'
        expected = _eval_single_bin(lhs_new, '&', rhs_new, self.engine)
        for ex in (ex1, ex2, ex3):
            result = pd.eval(ex, engine=self.engine, parser=self.parser)
            tm.assert_almost_equal(result, expected)