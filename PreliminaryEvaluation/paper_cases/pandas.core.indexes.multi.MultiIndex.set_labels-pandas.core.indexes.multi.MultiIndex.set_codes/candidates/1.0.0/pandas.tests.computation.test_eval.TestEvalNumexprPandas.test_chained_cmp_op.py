@pytest.mark.slow
def test_chained_cmp_op(self):
    mids = self.lhses
    cmp_ops = ('<', '>')
    for lhs, cmp1, mid, cmp2, rhs in product(self.lhses, cmp_ops, mids, cmp_ops, self.rhses):
        self.check_chained_cmp_op(lhs, cmp1, mid, cmp2, rhs)