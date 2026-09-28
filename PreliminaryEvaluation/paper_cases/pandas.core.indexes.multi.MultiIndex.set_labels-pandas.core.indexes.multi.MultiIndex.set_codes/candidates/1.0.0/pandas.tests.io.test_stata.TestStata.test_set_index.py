def test_set_index(self):
    df = tm.makeDataFrame()
    df.index.name = 'index'
    with tm.ensure_clean() as path:
        df.to_stata(path)
        reread = pd.read_stata(path, index_col='index')
    tm.assert_frame_equal(df, reread)