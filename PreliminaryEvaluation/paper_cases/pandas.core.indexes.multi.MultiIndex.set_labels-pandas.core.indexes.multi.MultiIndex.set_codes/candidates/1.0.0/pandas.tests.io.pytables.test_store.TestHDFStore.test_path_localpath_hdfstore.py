def test_path_localpath_hdfstore(self, setup_path):
    df = tm.makeDataFrame()

    def writer(path):
        with pd.HDFStore(path) as store:
            df.to_hdf(store, 'df')

    def reader(path):
        with pd.HDFStore(path) as store:
            return pd.read_hdf(store, 'df')
    result = tm.round_trip_localpath(writer, reader)
    tm.assert_frame_equal(df, result)