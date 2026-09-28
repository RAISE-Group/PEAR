def test_simple_bool_ops(self):
    for op, lhs, rhs in product(expr._bool_ops_syms, (True, False), (True, False)):
        ex = f'lhs {op} rhs'
        if op in ('and', 'or'):
            with pytest.raises(NotImplementedError):
                pd.eval(ex, engine=self.engine, parser=self.parser)
        else:
            res = pd.eval(ex, engine=self.engine, parser=self.parser)
            exp = eval(ex)
            assert res == exp