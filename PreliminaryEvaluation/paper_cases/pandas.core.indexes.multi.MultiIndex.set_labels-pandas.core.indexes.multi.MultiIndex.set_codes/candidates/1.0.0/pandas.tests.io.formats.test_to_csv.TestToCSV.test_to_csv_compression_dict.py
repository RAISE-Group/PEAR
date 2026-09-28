def test_to_csv_compression_dict(self, compression_only):
    method = compression_only
    df = DataFrame({'ABC': [1]})
    filename = 'to_csv_compress_as_dict.'
    filename += 'gz' if method == 'gzip' else method
    with tm.ensure_clean(filename) as path:
        df.to_csv(path, compression={'method': method})
        read_df = pd.read_csv(path, index_col=0)
        tm.assert_frame_equal(read_df, df)