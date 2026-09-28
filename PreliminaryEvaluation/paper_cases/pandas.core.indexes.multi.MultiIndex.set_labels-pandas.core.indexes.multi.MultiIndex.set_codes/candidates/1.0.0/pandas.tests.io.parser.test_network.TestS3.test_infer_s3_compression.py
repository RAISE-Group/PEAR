def test_infer_s3_compression(self, tips_df):
    for ext in ['', '.gz', '.bz2']:
        df = read_csv('s3://pandas-test/tips.csv' + ext, engine='python', compression='infer')
        assert isinstance(df, DataFrame)
        assert not df.empty
        tm.assert_frame_equal(df, tips_df)