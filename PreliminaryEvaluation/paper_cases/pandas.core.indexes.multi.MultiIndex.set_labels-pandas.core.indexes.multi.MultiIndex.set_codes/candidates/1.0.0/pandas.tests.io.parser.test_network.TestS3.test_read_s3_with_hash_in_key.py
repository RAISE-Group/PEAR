def test_read_s3_with_hash_in_key(self, tips_df):
    result = read_csv('s3://pandas-test/tips#1.csv')
    tm.assert_frame_equal(tips_df, result)