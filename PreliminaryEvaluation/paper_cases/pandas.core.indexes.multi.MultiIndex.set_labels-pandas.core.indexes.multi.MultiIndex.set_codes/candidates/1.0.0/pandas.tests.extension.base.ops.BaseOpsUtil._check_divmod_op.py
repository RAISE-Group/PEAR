def _check_divmod_op(self, s, op, other, exc=Exception):
    if exc is None:
        result_div, result_mod = op(s, other)
        if op is divmod:
            expected_div, expected_mod = (s // other, s % other)
        else:
            expected_div, expected_mod = (other // s, other % s)
        self.assert_series_equal(result_div, expected_div)
        self.assert_series_equal(result_mod, expected_mod)
    else:
        with pytest.raises(exc):
            divmod(s, other)