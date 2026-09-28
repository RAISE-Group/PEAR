def test_nested_raises_on_local_self_reference(self):
    from pandas.core.computation.ops import UndefinedVariableError
    df = DataFrame(np.random.randn(5, 3))
    with pytest.raises(UndefinedVariableError, match="name 'df' is not defined"):
        df.query('df > 0', engine=self.engine, parser=self.parser)