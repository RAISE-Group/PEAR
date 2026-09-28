def test_concat_tz_frame(self):
    df2 = DataFrame(dict(A=pd.Timestamp('20130102', tz='US/Eastern'), B=pd.Timestamp('20130603', tz='CET')), index=range(5))
    df3 = pd.concat([df2.A.to_frame(), df2.B.to_frame()], axis=1)
    tm.assert_frame_equal(df2, df3)