def test_to_csv_compression_dict_no_method_raises(self):
    df = DataFrame({'ABC': [1]})
    compression = {'some_option': True}
    msg = "must have key 'method'"
    with tm.ensure_clean('out.zip') as path:
        with pytest.raises(ValueError, match=msg):
            df.to_csv(path, compression=compression)