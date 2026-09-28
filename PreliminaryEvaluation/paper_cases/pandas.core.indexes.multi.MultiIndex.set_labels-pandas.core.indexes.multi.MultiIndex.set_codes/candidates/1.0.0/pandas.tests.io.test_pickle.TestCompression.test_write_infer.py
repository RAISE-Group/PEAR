@pytest.mark.parametrize('ext', ['', '.gz', '.bz2', '.no_compress', '.xz'])
def test_write_infer(self, ext, get_random_path):
    base = get_random_path
    path1 = base + ext
    path2 = base + '.raw'
    compression = None
    for c in self._compression_to_extension:
        if self._compression_to_extension[c] == ext:
            compression = c
            break
    with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
        df = tm.makeDataFrame()
        df.to_pickle(p1)
        with tm.decompress_file(p1, compression=compression) as f:
            with open(p2, 'wb') as fh:
                fh.write(f.read())
        df2 = pd.read_pickle(p2, compression=None)
        tm.assert_frame_equal(df, df2)