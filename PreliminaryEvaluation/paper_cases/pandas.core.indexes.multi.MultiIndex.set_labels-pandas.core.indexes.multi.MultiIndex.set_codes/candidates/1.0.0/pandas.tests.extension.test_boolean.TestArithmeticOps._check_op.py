def _check_op(self, s, op, other, op_name, exc=NotImplementedError):
    if exc is None:
        if op_name in ('__sub__', '__rsub__'):
            if _np_version_under1p14:
                pytest.skip('__sub__ does not yet raise in numpy 1.13')
            with pytest.raises(TypeError):
                op(s, other)
            return
        result = op(s, other)
        expected = s.combine(other, op)
        if op_name in ('__floordiv__', '__rfloordiv__', '__pow__', '__rpow__', '__mod__', '__rmod__'):
            expected = expected.astype('Int8')
        elif op_name in ('__truediv__', '__rtruediv__'):
            expected = s.astype(float).combine(other, op)
        if op_name == '__rpow__':
            expected[result.isna()] = np.nan
        self.assert_series_equal(result, expected)
    else:
        with pytest.raises(exc):
            op(s, other)