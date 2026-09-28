def _check_logical_ops(self, a, b, a_dense, b_dense):
    self._check_bool_result(a & b)
    self._assert((a & b).to_dense(), a_dense & b_dense)
    self._check_bool_result(a | b)
    self._assert((a | b).to_dense(), a_dense | b_dense)
    self._check_bool_result(a & b_dense)
    self._assert((a & b_dense).to_dense(), a_dense & b_dense)
    self._check_bool_result(a | b_dense)
    self._assert((a | b_dense).to_dense(), a_dense | b_dense)