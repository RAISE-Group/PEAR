def test_pickle_path_localpath(self, setup_path):
    df = tm.makeDataFrame()
    result = tm.round_trip_pathlib(lambda p: df.to_hdf(p, 'df'), lambda p: pd.read_hdf(p, 'df'))
    tm.assert_frame_equal(df, result)