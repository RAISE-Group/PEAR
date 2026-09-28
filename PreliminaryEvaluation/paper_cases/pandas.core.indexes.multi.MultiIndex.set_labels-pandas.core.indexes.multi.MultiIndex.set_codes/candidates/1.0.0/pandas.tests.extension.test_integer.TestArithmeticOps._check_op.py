def _check_op(self, s, op, other, op_name, exc=NotImplementedError):
    if exc is None:
        if s.dtype.is_unsigned_integer and op_name == '__rsub__':
            pytest.skip('unsigned subtraction gives negative values')
        if hasattr(other, 'dtype') and (not is_extension_array_dtype(other.dtype)) and pd.api.types.is_integer_dtype(other.dtype):
            other = other.astype(s.dtype.numpy_dtype)
        result = op(s, other)
        expected = s.combine(other, op)
        if op_name in ('__rtruediv__', '__truediv__', '__div__'):
            expected = expected.fillna(np.nan).astype(float)
            if op_name == '__rtruediv__':
                result = result.astype(float)
        elif op_name.startswith('__r'):
            expected = expected.astype(s.dtype)
            result = result.astype(s.dtype)
        else:
            expected = expected.astype(s.dtype)
            pass
        if op_name == '__rpow__' and isinstance(other, pd.Series):
            result = result.fillna(1)
        self.assert_series_equal(result, expected)
    else:
        with pytest.raises(exc):
            op(s, other)