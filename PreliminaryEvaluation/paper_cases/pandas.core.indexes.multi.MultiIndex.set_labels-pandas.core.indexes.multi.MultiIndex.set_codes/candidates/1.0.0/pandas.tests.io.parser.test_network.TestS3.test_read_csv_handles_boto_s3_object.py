def test_read_csv_handles_boto_s3_object(self, s3_resource, tips_file):
    s3_object = s3_resource.meta.client.get_object(Bucket='pandas-test', Key='tips.csv')
    result = read_csv(BytesIO(s3_object['Body'].read()), encoding='utf8')
    assert isinstance(result, DataFrame)
    assert not result.empty
    expected = read_csv(tips_file)
    tm.assert_frame_equal(result, expected)