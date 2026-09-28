def test_arith_series_with_array(self, data, all_arithmetic_operators):
    op_name = all_arithmetic_operators
    s = pd.Series(data)
    context = decimal.getcontext()
    divbyzerotrap = context.traps[decimal.DivisionByZero]
    invalidoptrap = context.traps[decimal.InvalidOperation]
    context.traps[decimal.DivisionByZero] = 0
    context.traps[decimal.InvalidOperation] = 0
    other = pd.Series([int(d * 100) for d in data])
    self.check_opname(s, op_name, other)
    if 'mod' not in op_name:
        self.check_opname(s, op_name, s * 2)
    self.check_opname(s, op_name, 0)
    self.check_opname(s, op_name, 5)
    context.traps[decimal.DivisionByZero] = divbyzerotrap
    context.traps[decimal.InvalidOperation] = invalidoptrap