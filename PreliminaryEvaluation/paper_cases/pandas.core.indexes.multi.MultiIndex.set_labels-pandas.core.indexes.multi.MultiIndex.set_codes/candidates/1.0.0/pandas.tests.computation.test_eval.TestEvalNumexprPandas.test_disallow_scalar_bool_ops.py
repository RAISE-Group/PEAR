def test_disallow_scalar_bool_ops(self):
    exprs = ('1 or 2', '1 and 2')
    exprs += ('a and b', 'a or b')
    exprs += ('1 or 2 and (3 + 2) > 3',)
    exprs += ('2 * x > 2 or 1 and 2',)
    exprs += ('2 * df > 3 and 1 or a',)
    x, a, b, df = (np.random.randn(3), 1, 2, DataFrame(randn(3, 2)))
    for ex in exprs:
        with pytest.raises(NotImplementedError):
            pd.eval(ex, engine=self.engine, parser=self.parser)