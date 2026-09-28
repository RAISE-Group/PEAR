@td.skip_if_not_us_locale
def test_read_s3_jsonl(self, s3_resource):
    result = read_json('s3n://pandas-test/items.jsonl', lines=True)
    expected = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    tm.assert_frame_equal(result, expected)