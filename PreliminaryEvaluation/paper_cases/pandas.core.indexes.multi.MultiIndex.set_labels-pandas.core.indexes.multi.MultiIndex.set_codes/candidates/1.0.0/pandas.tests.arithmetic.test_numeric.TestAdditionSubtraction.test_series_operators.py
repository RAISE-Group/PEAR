def test_series_operators(self):

    def _check_op(series, other, op, pos_only=False, check_dtype=True):
        left = np.abs(series) if pos_only else series
        right = np.abs(other) if pos_only else other
        cython_or_numpy = op(left, right)
        python = left.combine(right, op)
        tm.assert_series_equal(cython_or_numpy, python, check_dtype=check_dtype)

    def check(series, other):
        simple_ops = ['add', 'sub', 'mul', 'truediv', 'floordiv', 'mod']
        for opname in simple_ops:
            _check_op(series, other, getattr(operator, opname))
        _check_op(series, other, operator.pow, pos_only=True)
        _check_op(series, other, ops.radd)
        _check_op(series, other, ops.rsub)
        _check_op(series, other, ops.rtruediv)
        _check_op(series, other, ops.rfloordiv)
        _check_op(series, other, ops.rmul)
        _check_op(series, other, ops.rpow, pos_only=True)
        _check_op(series, other, ops.rmod)
    tser = tm.makeTimeSeries().rename('ts')
    check(tser, tser * 2)
    check(tser, tser[::2])
    check(tser, 5)

    def check_comparators(series, other, check_dtype=True):
        _check_op(series, other, operator.gt, check_dtype=check_dtype)
        _check_op(series, other, operator.ge, check_dtype=check_dtype)
        _check_op(series, other, operator.eq, check_dtype=check_dtype)
        _check_op(series, other, operator.lt, check_dtype=check_dtype)
        _check_op(series, other, operator.le, check_dtype=check_dtype)
    check_comparators(tser, 5)
    check_comparators(tser, tser + 1, check_dtype=False)