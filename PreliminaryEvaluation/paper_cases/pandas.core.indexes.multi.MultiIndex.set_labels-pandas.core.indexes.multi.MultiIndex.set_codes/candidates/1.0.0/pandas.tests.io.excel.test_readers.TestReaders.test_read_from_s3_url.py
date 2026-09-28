@td.skip_if_not_us_locale
def test_read_from_s3_url(self, read_ext, s3_resource):
    with open('test1' + read_ext, 'rb') as f:
        s3_resource.Bucket('pandas-test').put_object(Key='test1' + read_ext, Body=f)
    url = 's3://pandas-test/test1' + read_ext
    url_table = pd.read_excel(url)
    local_table = pd.read_excel('test1' + read_ext)
    tm.assert_frame_equal(url_table, local_table)