def test_simple_arith_ops(self):
    ops = self.arith_ops
    for op in filter(lambda x: x != '//', ops):
        ex = f'1 {op} 1'
        ex2 = f'x {op} 1'
        ex3 = f'1 {op} (x + 1)'
        if op in ('in', 'not in'):
            msg = "argument of type 'int' is not iterable"
            with pytest.raises(TypeError, match=msg):
                pd.eval(ex, engine=self.engine, parser=self.parser)
        else:
            expec = _eval_single_bin(1, op, 1, self.engine)
            x = self.eval(ex, engine=self.engine, parser=self.parser)
            assert x == expec
            expec = _eval_single_bin(x, op, 1, self.engine)
            y = self.eval(ex2, local_dict={'x': x}, engine=self.engine, parser=self.parser)
            assert y == expec
            expec = _eval_single_bin(1, op, x + 1, self.engine)
            y = self.eval(ex3, local_dict={'x': x}, engine=self.engine, parser=self.parser)
            assert y == expec