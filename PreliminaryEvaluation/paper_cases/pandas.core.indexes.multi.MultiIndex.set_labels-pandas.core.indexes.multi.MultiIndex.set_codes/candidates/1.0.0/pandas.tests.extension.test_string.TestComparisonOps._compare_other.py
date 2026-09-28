def _compare_other(self, s, data, op_name, other):
    result = getattr(s, op_name)(other)
    expected = getattr(s.astype(object), op_name)(other).astype('boolean')
    self.assert_series_equal(result, expected)