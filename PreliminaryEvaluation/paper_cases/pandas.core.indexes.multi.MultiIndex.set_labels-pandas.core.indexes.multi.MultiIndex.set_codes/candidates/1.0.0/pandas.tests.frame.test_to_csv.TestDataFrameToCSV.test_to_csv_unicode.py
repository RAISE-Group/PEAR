def test_to_csv_unicode(self):
    df = DataFrame({'c/σ': [1, 2, 3]})
    with tm.ensure_clean() as path:
        df.to_csv(path, encoding='UTF-8')
        df2 = read_csv(path, index_col=0, encoding='UTF-8')
        tm.assert_frame_equal(df, df2)
        df.to_csv(path, encoding='UTF-8', index=False)
        df2 = read_csv(path, index_col=None, encoding='UTF-8')
        tm.assert_frame_equal(df, df2)