def test_date_index_query_with_NaT_duplicates(self):
    engine, parser = (self.engine, self.parser)
    n = 10
    df = DataFrame(np.random.randn(n, 3))
    df['dates1'] = date_range('1/1/2012', periods=n)
    df['dates3'] = date_range('1/1/2014', periods=n)
    df.loc[np.random.rand(n) > 0.5, 'dates1'] = pd.NaT
    df.set_index('dates1', inplace=True, drop=True)
    with pytest.raises(NotImplementedError):
        df.query('index < 20130101 < dates3', engine=engine, parser=parser)