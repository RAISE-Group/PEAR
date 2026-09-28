def check_floor_division(self, lhs, arith1, rhs):
    ex = f'lhs {arith1} rhs'
    if self.engine == 'python':
        res = pd.eval(ex, engine=self.engine, parser=self.parser)
        expected = lhs // rhs
        self.check_equal(res, expected)
    else:
        msg = "unsupported operand type\\(s\\) for //: 'VariableNode' and 'VariableNode'"
        with pytest.raises(TypeError, match=msg):
            pd.eval(ex, local_dict={'lhs': lhs, 'rhs': rhs}, engine=self.engine, parser=self.parser)