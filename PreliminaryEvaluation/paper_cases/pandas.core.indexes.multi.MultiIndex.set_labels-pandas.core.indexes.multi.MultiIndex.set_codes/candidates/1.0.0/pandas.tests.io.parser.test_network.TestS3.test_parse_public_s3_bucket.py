def test_parse_public_s3_bucket(self, tips_df):
    pytest.importorskip('s3fs')
    for ext, comp in [('', None), ('.gz', 'gzip'), ('.bz2', 'bz2')]:
        df = read_csv('s3://pandas-test/tips.csv' + ext, compression=comp)
        assert isinstance(df, DataFrame)
        assert not df.empty
        tm.assert_frame_equal(df, tips_df)
    df = read_csv('s3://cant_get_it/tips.csv')
    assert isinstance(df, DataFrame)
    assert not df.empty
    tm.assert_frame_equal(df, tips_df)