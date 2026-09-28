def test_s3_fails(self):
    with pytest.raises(IOError):
        read_csv('s3://nyqpug/asdf.csv')
    with pytest.raises(IOError):
        read_csv('s3://cant_get_it/file.csv')