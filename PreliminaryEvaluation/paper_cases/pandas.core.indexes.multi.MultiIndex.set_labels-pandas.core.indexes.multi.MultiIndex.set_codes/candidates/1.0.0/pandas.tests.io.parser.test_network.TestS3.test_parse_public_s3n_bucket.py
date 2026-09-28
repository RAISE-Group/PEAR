def test_parse_public_s3n_bucket(self, tips_df):
    df = read_csv('s3n://pandas-test/tips.csv', nrows=10)
    assert isinstance(df, DataFrame)
    assert not df.empty
    tm.assert_frame_equal(tips_df.iloc[:10], df)