def test_date_query_with_non_date(self):
    engine, parser = (self.engine, self.parser)
    n = 10
    df = DataFrame({'dates': date_range('1/1/2012', periods=n), 'nondate': np.arange(n)})
    result = df.query('dates == nondate', parser=parser, engine=engine)
    assert len(result) == 0
    result = df.query('dates != nondate', parser=parser, engine=engine)
    tm.assert_frame_equal(result, df)
    for op in ['<', '>', '<=', '>=']:
        with pytest.raises(TypeError):
            df.query('dates {op} nondate'.format(op=op), parser=parser, engine=engine)