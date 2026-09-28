def test_gzip_writing(self):
    df = tm.makeDataFrame()
    df.index.name = 'index'
    with tm.ensure_clean() as path:
        with gzip.GzipFile(path, 'wb') as gz:
            df.to_stata(gz, version=114)
        with gzip.GzipFile(path, 'rb') as gz:
            reread = pd.read_stata(gz, index_col='index')
    tm.assert_frame_equal(df, reread)