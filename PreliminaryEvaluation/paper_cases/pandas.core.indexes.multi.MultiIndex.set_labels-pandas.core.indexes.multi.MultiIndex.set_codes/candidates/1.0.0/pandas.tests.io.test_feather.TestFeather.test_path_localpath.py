def test_path_localpath(self):
    df = tm.makeDataFrame().reset_index()
    result = tm.round_trip_localpath(df.to_feather, pd.read_feather)
    tm.assert_frame_equal(df, result)