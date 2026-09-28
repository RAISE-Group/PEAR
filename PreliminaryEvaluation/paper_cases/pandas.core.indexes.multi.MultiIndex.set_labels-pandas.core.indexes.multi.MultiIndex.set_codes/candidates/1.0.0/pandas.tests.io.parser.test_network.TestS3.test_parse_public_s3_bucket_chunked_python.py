def test_parse_public_s3_bucket_chunked_python(self, tips_df):
    chunksize = 5
    for ext, comp in [('', None), ('.gz', 'gzip'), ('.bz2', 'bz2')]:
        df_reader = read_csv('s3://pandas-test/tips.csv' + ext, chunksize=chunksize, compression=comp, engine='python')
        assert df_reader.chunksize == chunksize
        for i_chunk in [0, 1, 2]:
            df = df_reader.get_chunk()
            assert isinstance(df, DataFrame)
            assert not df.empty
            true_df = tips_df.iloc[chunksize * i_chunk:chunksize * (i_chunk + 1)]
            tm.assert_frame_equal(true_df, df)