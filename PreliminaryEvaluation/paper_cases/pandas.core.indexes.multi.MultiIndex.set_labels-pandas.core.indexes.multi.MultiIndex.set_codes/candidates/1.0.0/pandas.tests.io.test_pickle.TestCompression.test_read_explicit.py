def test_read_explicit(self, compression, get_random_path):
    base = get_random_path
    path1 = base + '.raw'
    path2 = base + '.compressed'
    with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
        df = tm.makeDataFrame()
        df.to_pickle(p1, compression=None)
        self.compress_file(p1, p2, compression=compression)
        df2 = pd.read_pickle(p2, compression=compression)
        tm.assert_frame_equal(df, df2)