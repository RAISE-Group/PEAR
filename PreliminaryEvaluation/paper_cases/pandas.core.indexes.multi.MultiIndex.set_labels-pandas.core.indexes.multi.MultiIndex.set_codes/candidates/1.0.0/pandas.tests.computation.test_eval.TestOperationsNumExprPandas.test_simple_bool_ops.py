def test_simple_bool_ops(self):
    for op, lhs, rhs in product(expr._bool_ops_syms, (True, False), (True, False)):
        ex = f'{lhs} {op} {rhs}'
        res = self.eval(ex)
        exp = eval(ex)
        assert res == exp