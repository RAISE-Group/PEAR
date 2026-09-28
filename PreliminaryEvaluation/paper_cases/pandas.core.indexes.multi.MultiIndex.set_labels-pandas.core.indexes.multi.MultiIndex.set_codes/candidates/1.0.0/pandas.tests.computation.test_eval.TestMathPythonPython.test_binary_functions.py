def test_binary_functions(self):
    df = DataFrame({'a': np.random.randn(10), 'b': np.random.randn(10)})
    a = df.a
    b = df.b
    for fn in self.binary_fns:
        expr = f'{fn}(a, b)'
        got = self.eval(expr)
        with np.errstate(all='ignore'):
            expect = getattr(np, fn)(a, b)
        tm.assert_almost_equal(got, expect, check_names=False)