@pytest.mark.parametrize('ext', ['', '.gz', '.bz2', '.zip', '.no_compress', '.xz'])
def test_read_infer(self, ext, get_random_path):
    base = get_random_path
    path1 = base + '.raw'
    path2 = base + ext
    compression = None
    for c in self._compression_to_extension:
        if self._compression_to_extension[c] == ext:
            compression = c
            break
    with tm.ensure_clean(path1) as p1, tm.ensure_clean(path2) as p2:
        df = tm.makeDataFrame()
        df.to_pickle(p1, compression=None)
        self.compress_file(p1, p2, compression=compression)
        df2 = pd.read_pickle(p2)
        tm.assert_frame_equal(df, df2)