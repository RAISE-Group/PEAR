def _check_divmod_op(self, s, op, other, exc=NotImplementedError):
    super()._check_divmod_op(s, op, other, exc=TypeError)