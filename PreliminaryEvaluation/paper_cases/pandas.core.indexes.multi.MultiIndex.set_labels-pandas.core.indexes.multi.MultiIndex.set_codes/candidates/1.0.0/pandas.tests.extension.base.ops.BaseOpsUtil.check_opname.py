def check_opname(self, s, op_name, other, exc=Exception):
    op = self.get_op_from_name(op_name)
    self._check_op(s, op, other, op_name, exc)