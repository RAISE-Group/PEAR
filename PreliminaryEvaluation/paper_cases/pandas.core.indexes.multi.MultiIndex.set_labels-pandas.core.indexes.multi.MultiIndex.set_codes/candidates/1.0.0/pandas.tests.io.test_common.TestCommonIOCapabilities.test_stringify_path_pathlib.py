def test_stringify_path_pathlib(self):
    rel_path = icom.stringify_path(Path('.'))
    assert rel_path == '.'
    redundant_path = icom.stringify_path(Path('foo//bar'))
    assert redundant_path == os.path.join('foo', 'bar')