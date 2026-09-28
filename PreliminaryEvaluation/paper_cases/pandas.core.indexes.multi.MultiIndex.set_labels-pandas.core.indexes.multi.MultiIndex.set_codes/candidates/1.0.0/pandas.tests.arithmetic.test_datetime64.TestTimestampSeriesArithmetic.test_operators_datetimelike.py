def test_operators_datetimelike(self):
    td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
    td1.iloc[2] = np.nan
    dt1 = Series([pd.Timestamp('20111230'), pd.Timestamp('20120101'), pd.Timestamp('20120103')])
    dt1.iloc[2] = np.nan
    dt2 = Series([pd.Timestamp('20111231'), pd.Timestamp('20120102'), pd.Timestamp('20120104')])
    dt1 - dt2
    dt2 - dt1
    dt1 + td1
    td1 + dt1
    dt1 - td1
    td1 + dt1
    dt1 + td1