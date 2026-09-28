def test_date_index_query_with_NaT(self):
    engine, parser = (self.engine, self.parser)
    n = 10
    df = DataFrame(np.random.randn(n, 3))
    df['dates1'] = date_range('1/1/2012', periods=n)
    df['dates3'] = date_range('1/1/2014', periods=n)
    df.iloc[0, 0] = pd.NaT
    df.set_index('dates1', inplace=True, drop=True)
    res = df.query('(index < 20130101) & (20130101 < dates3)', engine=engine, parser=parser)
    expec = df[(df.index < '20130101') & ('20130101' < df.dates3)]
    tm.assert_frame_equal(res, expec)