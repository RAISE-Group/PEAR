def test_undefined_func(self):
    df = DataFrame({'a': np.random.randn(10)})
    msg = '"mysin" is not a supported function'
    with pytest.raises(ValueError, match=msg):
        df.eval('mysin(a)', engine=self.engine, parser=self.parser)