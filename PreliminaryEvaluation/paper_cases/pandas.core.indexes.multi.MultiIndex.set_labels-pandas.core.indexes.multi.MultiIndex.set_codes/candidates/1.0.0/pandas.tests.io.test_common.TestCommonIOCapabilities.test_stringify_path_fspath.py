def test_stringify_path_fspath(self):
    p = CustomFSPath('foo/bar.csv')
    result = icom.stringify_path(p)
    assert result == 'foo/bar.csv'