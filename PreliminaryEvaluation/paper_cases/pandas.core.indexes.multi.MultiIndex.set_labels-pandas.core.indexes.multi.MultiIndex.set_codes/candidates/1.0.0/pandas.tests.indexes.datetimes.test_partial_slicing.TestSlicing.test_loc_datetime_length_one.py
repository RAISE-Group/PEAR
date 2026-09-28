def test_loc_datetime_length_one(self):
    df = pd.DataFrame(columns=['1'], index=pd.date_range('2016-10-01T00:00:00', '2016-10-01T23:59:59'))
    result = df.loc[datetime(2016, 10, 1):]
    tm.assert_frame_equal(result, df)
    result = df.loc['2016-10-01T00:00:00':]
    tm.assert_frame_equal(result, df)