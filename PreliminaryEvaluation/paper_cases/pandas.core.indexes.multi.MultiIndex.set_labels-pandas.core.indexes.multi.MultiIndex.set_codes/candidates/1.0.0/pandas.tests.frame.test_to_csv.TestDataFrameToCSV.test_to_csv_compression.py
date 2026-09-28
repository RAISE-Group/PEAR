@pytest.mark.parametrize('df,encoding', [(DataFrame([[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]], index=['A', 'B'], columns=['X', 'Y', 'Z']), None), (DataFrame([['abc', 'def', 'ghi']], columns=['X', 'Y', 'Z']), 'ascii'), (DataFrame(5 * [[123, '你好', '世界']], columns=['X', 'Y', 'Z']), 'gb2312'), (DataFrame(5 * [[123, 'Γειά σου', 'Κόσμε']], columns=['X', 'Y', 'Z']), 'cp737')])
def test_to_csv_compression(self, df, encoding, compression):
    with tm.ensure_clean() as filename:
        df.to_csv(filename, compression=compression, encoding=encoding)
        result = read_csv(filename, compression=compression, index_col=0, encoding=encoding)
        tm.assert_frame_equal(df, result)
        f, _handles = get_handle(filename, 'w', compression=compression, encoding=encoding)
        with f:
            df.to_csv(f, encoding=encoding)
        result = pd.read_csv(filename, compression=compression, encoding=encoding, index_col=0, squeeze=True)
        tm.assert_frame_equal(df, result)
        with tm.decompress_file(filename, compression) as fh:
            text = fh.read().decode(encoding or 'utf8')
            for col in df.columns:
                assert col in text
        with tm.decompress_file(filename, compression) as fh:
            tm.assert_frame_equal(df, read_csv(fh, index_col=0, encoding=encoding))