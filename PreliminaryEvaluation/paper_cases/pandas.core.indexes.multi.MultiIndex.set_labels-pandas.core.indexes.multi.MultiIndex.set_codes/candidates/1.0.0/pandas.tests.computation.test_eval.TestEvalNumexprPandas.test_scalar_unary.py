def test_scalar_unary(self):
    with pytest.raises(TypeError):
        pd.eval('~1.0', engine=self.engine, parser=self.parser)
    assert pd.eval('-1.0', parser=self.parser, engine=self.engine) == -1.0
    assert pd.eval('+1.0', parser=self.parser, engine=self.engine) == +1.0
    assert pd.eval('~1', parser=self.parser, engine=self.engine) == ~1
    assert pd.eval('-1', parser=self.parser, engine=self.engine) == -1
    assert pd.eval('+1', parser=self.parser, engine=self.engine) == +1
    assert pd.eval('~True', parser=self.parser, engine=self.engine) == ~True
    assert pd.eval('~False', parser=self.parser, engine=self.engine) == ~False
    assert pd.eval('-True', parser=self.parser, engine=self.engine) == -True
    assert pd.eval('-False', parser=self.parser, engine=self.engine) == -False
    assert pd.eval('+True', parser=self.parser, engine=self.engine) == +True
    assert pd.eval('+False', parser=self.parser, engine=self.engine) == +False