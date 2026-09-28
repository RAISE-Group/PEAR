def _compare_other(self, s, data, op_name, other):
    op = self.get_op_from_name(op_name)
    result = pd.Series(op(data, other))
    assert isinstance(result.dtype, SparseDtype)
    assert result.dtype.subtype == np.dtype('bool')
    with np.errstate(all='ignore'):
        expected = pd.Series(SparseArray(op(np.asarray(data), np.asarray(other)), fill_value=result.values.fill_value))
    tm.assert_series_equal(result, expected)
    s = pd.Series(data)
    result = op(s, other)
    tm.assert_series_equal(result, expected)