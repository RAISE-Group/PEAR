def test_pickle_path_localpath(self):
    df = tm.makeDataFrame()
    df.index.name = 'index'
    reader = lambda x: read_stata(x).set_index('index')
    result = tm.round_trip_localpath(df.to_stata, reader)
    tm.assert_frame_equal(df, result)