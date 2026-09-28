def test_bool_ops_with_constants(self):
    for op, lhs, rhs in product(expr._bool_ops_syms, ('True', 'False'), ('True', 'False')):
        ex = f'{lhs} {op} {rhs}'
        if op in ('and', 'or'):
            with pytest.raises(NotImplementedError):
                self.eval(ex)
        else:
            res = self.eval(ex)
            exp = eval(ex)
            assert res == exp