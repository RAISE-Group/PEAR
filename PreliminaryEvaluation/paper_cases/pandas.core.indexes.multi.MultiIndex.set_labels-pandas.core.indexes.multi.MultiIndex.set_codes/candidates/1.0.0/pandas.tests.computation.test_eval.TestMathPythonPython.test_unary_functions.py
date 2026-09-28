def test_unary_functions(self, unary_fns_for_ne):
    df = DataFrame({'a': np.random.randn(10)})
    a = df.a
    for fn in unary_fns_for_ne:
        expr = f'{fn}(a)'
        got = self.eval(expr)
        with np.errstate(all='ignore'):
            expect = getattr(np, fn)(a)
        tm.assert_series_equal(got, expect, check_names=False)