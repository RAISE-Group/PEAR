def _check_op(self, s, op, other, op_name, exc=NotImplementedError):
    if exc is None:
        result = op(s, other)
        expected = s.combine(other, op)
        self.assert_series_equal(result, expected)
    else:
        with pytest.raises(exc):
            op(s, other)