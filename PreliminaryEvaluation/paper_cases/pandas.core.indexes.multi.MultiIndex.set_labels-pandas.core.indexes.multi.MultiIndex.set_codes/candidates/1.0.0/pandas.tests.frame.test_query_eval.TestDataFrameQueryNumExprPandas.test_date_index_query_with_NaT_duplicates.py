def test_date_index_query_with_NaT_duplicates(self):
    engine, parser = (self.engine, self.parser)
    n = 10
    d = {}
    d['dates1'] = date_range('1/1/2012', periods=n)
    d['dates3'] = date_range('1/1/2014', periods=n)
    df = DataFrame(d)
    df.loc[np.random.rand(n) > 0.5, 'dates1'] = pd.NaT
    df.set_index('dates1', inplace=True, drop=True)
    res = df.query('dates1 < 20130101 < dates3', engine=engine, parser=parser)
    expec = df[(df.index.to_series() < '20130101') & ('20130101' < df.dates3)]
    tm.assert_frame_equal(res, expec)