@pytest.mark.slow
def test_binary_arith_ops(self):
    for lhs, op, rhs in product(self.lhses, self.arith_ops, self.rhses):
        self.check_binary_arith_op(lhs, op, rhs)