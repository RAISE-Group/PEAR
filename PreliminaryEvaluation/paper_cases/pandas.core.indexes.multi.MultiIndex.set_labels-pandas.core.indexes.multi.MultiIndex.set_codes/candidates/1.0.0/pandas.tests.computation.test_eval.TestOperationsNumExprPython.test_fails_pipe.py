def test_fails_pipe(self):
    df = DataFrame(np.random.randn(5, 3))
    ex = '(df + 2)[df > 1] > 0 | (df > 0)'
    with pytest.raises(NotImplementedError):
        pd.eval(ex, parser=self.parser, engine=self.engine)