def test_floor_and_ceil_functions_raise_error(self, ne_lt_2_6_9, unary_fns_for_ne):
    for fn in ('floor', 'ceil'):
        msg = f'"{fn}" is not a supported function'
        with pytest.raises(ValueError, match=msg):
            expr = f'{fn}(100)'
            self.eval(expr)