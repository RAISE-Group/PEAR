def test_keyword_arg(self):
    df = DataFrame({'a': np.random.randn(10)})
    msg = 'Function "sin" does not support keyword arguments'
    with pytest.raises(TypeError, match=msg):
        df.eval('sin(x=a)', engine=self.engine, parser=self.parser)