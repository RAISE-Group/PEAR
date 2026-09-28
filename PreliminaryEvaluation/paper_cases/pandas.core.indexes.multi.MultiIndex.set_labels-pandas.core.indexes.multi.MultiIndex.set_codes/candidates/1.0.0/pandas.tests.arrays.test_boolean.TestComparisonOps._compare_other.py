def _compare_other(self, data, op_name, other):
    op = self.get_op_from_name(op_name)
    result = pd.Series(op(data, other))
    expected = pd.Series(op(data._data, other), dtype='boolean')
    expected[data._mask] = pd.NA
    tm.assert_series_equal(result, expected)
    s = pd.Series(data)
    result = op(s, other)
    expected = pd.Series(data._data)
    expected = op(expected, other)
    expected = expected.astype('boolean')
    expected[data._mask] = pd.NA
    tm.assert_series_equal(result, expected)