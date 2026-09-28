@pytest.mark.parametrize('s,encoding', [(Series([0.123456, 0.234567, 0.567567], index=['A', 'B', 'C'], name='X'), None), (Series(['abc', 'def', 'ghi'], name='X'), 'ascii'), (Series(['123', '你好', '世界'], name='中文'), 'gb2312'), (Series(['123', 'Γειά σου', 'Κόσμε'], name='Ελληνικά'), 'cp737')])
def test_to_csv_compression(self, s, encoding, compression):
    with tm.ensure_clean() as filename:
        s.to_csv(filename, compression=compression, encoding=encoding, header=True)
        result = pd.read_csv(filename, compression=compression, encoding=encoding, index_col=0, squeeze=True)
        tm.assert_series_equal(s, result)
        f, _handles = get_handle(filename, 'w', compression=compression, encoding=encoding)
        with f:
            s.to_csv(f, encoding=encoding, header=True)
        result = pd.read_csv(filename, compression=compression, encoding=encoding, index_col=0, squeeze=True)
        tm.assert_series_equal(s, result)
        with tm.decompress_file(filename, compression) as fh:
            text = fh.read().decode(encoding or 'utf8')
            assert s.name in text
        with tm.decompress_file(filename, compression) as fh:
            tm.assert_series_equal(s, pd.read_csv(fh, index_col=0, squeeze=True, encoding=encoding))