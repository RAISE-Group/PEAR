def _combine_frame(self, other, func, fill_value=None, level=None):
    if fill_value is None:
        _arith_op = func
    else:

        def _arith_op(left, right):
            left, right = ops.fill_binop(left, right, fill_value)
            return func(left, right)
    if ops.should_series_dispatch(self, other, func):
        new_data = ops.dispatch_to_series(self, other, _arith_op)
    else:
        with np.errstate(all='ignore'):
            res_values = _arith_op(self.values, other.values)
        new_data = dispatch_fill_zeros(func, self.values, other.values, res_values)
    return new_data