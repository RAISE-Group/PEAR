def test_write_explicit(self, compression, get_random_path):
    base = get_random_path
    path1 = base + '.compressed'
    path2 = base + '.raw'
    with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
        df = tm.makeDataFrame()
        df.to_pickle(p1, compression=compression)
        with tm.decompress_file(p1, compression=compression) as f:
            with open(p2, 'wb') as fh:
                fh.write(f.read())
        df2 = pd.read_pickle(p2, compression=None)
        tm.assert_frame_equal(df, df2)