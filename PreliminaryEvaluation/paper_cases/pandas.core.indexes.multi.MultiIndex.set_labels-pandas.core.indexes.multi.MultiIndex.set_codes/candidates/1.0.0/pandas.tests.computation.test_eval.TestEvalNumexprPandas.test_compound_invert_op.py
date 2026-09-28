@pytest.mark.slow
def test_compound_invert_op(self):
    for lhs, op, rhs in product(self.lhses, self.cmp_ops, self.rhses):
        self.check_compound_invert_op(lhs, op, rhs)