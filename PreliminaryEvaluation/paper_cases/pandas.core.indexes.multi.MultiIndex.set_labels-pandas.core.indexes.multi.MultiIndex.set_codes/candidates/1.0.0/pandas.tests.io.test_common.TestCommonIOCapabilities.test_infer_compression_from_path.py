@pytest.mark.parametrize('extension,expected', [('', None), ('.gz', 'gzip'), ('.bz2', 'bz2'), ('.zip', 'zip'), ('.xz', 'xz')])
@pytest.mark.parametrize('path_type', path_types)
def test_infer_compression_from_path(self, extension, expected, path_type):
    path = path_type('foo/bar.csv' + extension)
    compression = icom.infer_compression(path, compression='infer')
    assert compression == expected