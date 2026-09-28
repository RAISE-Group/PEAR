def test_path_local_path(self, engine, ext):
    df = tm.makeDataFrame()
    writer = partial(df.to_excel, engine=engine)
    reader = partial(pd.read_excel, index_col=0)
    result = tm.round_trip_pathlib(writer, reader, path='foo.{ext}'.format(ext=ext))
    tm.assert_frame_equal(result, df)