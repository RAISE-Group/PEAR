def test_query_syntax_error(self):
    engine, parser = (self.engine, self.parser)
    df = DataFrame({'i': range(10), '+': range(3, 13), 'r': range(4, 14)})
    with pytest.raises(SyntaxError):
        df.query('i - +', engine=engine, parser=parser)