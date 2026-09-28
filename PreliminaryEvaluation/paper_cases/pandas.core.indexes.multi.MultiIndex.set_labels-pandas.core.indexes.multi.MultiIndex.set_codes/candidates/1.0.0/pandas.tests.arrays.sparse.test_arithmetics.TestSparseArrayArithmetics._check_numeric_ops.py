def _check_numeric_ops(self, a, b, a_dense, b_dense, mix, op):
    with np.errstate(invalid='ignore', divide='ignore'):
        if op in [operator.floordiv, ops.rfloordiv]:
            if self._base == pd.Series and a.dtype.subtype == np.dtype('int64'):
                pytest.xfail('Not defined/working.  See GH#13843')
        if mix:
            result = op(a, b_dense).to_dense()
        else:
            result = op(a, b).to_dense()
        if op in [operator.truediv, ops.rtruediv]:
            expected = op(a_dense * 1.0, b_dense)
        else:
            expected = op(a_dense, b_dense)
        if op in [operator.floordiv, ops.rfloordiv]:
            mask = np.isinf(expected)
            if mask.any():
                expected[mask] = np.nan
        self._assert(result, expected)