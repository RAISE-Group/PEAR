def test_simple_cmp_ops(self):
    bool_lhses = (DataFrame(tm.randbool(size=(10, 5))), Series(tm.randbool((5,))), tm.randbool())
    bool_rhses = (DataFrame(tm.randbool(size=(10, 5))), Series(tm.randbool((5,))), tm.randbool())
    for lhs, rhs, cmp_op in product(bool_lhses, bool_rhses, self.cmp_ops):
        self.check_simple_cmp_op(lhs, cmp_op, rhs)