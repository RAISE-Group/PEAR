def test_fillna_tzaware(self):
    df = pd.DataFrame({'A': [pd.Timestamp('2012-11-11 00:00:00+01:00'), pd.NaT]})
    exp = pd.DataFrame({'A': [pd.Timestamp('2012-11-11 00:00:00+01:00'), pd.Timestamp('2012-11-11 00:00:00+01:00')]})
    tm.assert_frame_equal(df.fillna(method='pad'), exp)
    df = pd.DataFrame({'A': [pd.NaT, pd.Timestamp('2012-11-11 00:00:00+01:00')]})
    exp = pd.DataFrame({'A': [pd.Timestamp('2012-11-11 00:00:00+01:00'), pd.Timestamp('2012-11-11 00:00:00+01:00')]})
    tm.assert_frame_equal(df.fillna(method='bfill'), exp)