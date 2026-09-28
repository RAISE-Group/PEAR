def test_parse_public_s3_bucket_python(self, tips_df):
    for ext, comp in [('', None), ('.gz', 'gzip'), ('.bz2', 'bz2')]:
        df = read_csv('s3://pandas-test/tips.csv' + ext, engine='python', compression=comp)
        assert isinstance(df, DataFrame)
        assert not df.empty
        tm.assert_frame_equal(df, tips_df)