def test_query_doesnt_pickup_local(self):
    from pandas.core.computation.ops import UndefinedVariableError
    engine, parser = (self.engine, self.parser)
    n = m = 10
    df = DataFrame(np.random.randint(m, size=(n, 3)), columns=list('abc'))
    with pytest.raises(UndefinedVariableError, match="name 'sin' is not defined"):
        df.query('sin > 5', engine=engine, parser=parser)