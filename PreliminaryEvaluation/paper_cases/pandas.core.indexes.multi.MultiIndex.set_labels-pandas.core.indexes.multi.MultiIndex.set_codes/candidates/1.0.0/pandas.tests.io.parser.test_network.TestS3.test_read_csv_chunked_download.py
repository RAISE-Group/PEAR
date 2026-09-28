def test_read_csv_chunked_download(self, s3_resource, caplog):
    import s3fs
    df = DataFrame(np.random.randn(100000, 4), columns=list('abcd'))
    buf = BytesIO()
    str_buf = StringIO()
    df.to_csv(str_buf)
    buf = BytesIO(str_buf.getvalue().encode('utf-8'))
    s3_resource.Bucket('pandas-test').put_object(Key='large-file.csv', Body=buf)
    s3fs.S3FileSystem.clear_instance_cache()
    with caplog.at_level(logging.DEBUG, logger='s3fs'):
        read_csv('s3://pandas-test/large-file.csv', nrows=5)
        assert (0, 5505024) in (x.args[-2:] for x in caplog.records)