def setup_ops(self):
    self.cmp_ops = list(filter(lambda x: x not in ('in', 'not in'), expr._cmp_ops_syms))
    self.cmp2_ops = self.cmp_ops[::-1]
    self.bin_ops = [s for s in expr._bool_ops_syms if s not in ('and', 'or')]
    self.special_case_ops = _special_case_arith_ops_syms
    self.arith_ops = _good_arith_ops
    self.unary_ops = ('+', '-', '~')