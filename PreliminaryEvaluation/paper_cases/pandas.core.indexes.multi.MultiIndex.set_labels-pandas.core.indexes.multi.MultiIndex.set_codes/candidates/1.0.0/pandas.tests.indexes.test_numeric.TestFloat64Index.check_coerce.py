def check_coerce(self, a, b, is_float_index=True):
    assert a.equals(b)
    tm.assert_index_equal(a, b, exact=False)
    if is_float_index:
        assert isinstance(b, Float64Index)
    else:
        self.check_is_index(b)