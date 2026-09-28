def setup_ops(self):
    self.cmp_ops = expr._cmp_ops_syms
    self.cmp2_ops = self.cmp_ops[::-1]
    self.bin_ops = expr._bool_ops_syms
    self.special_case_ops = _special_case_arith_ops_syms
    self.arith_ops = _good_arith_ops
    self.unary_ops = ('-', '~', 'not ')