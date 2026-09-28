@td.skip_if_no('py.path')
def test_stringify_path_localpath(self):
    path = os.path.join('foo', 'bar')
    abs_path = os.path.abspath(path)
    lpath = LocalPath(path)
    assert icom.stringify_path(lpath) == abs_path