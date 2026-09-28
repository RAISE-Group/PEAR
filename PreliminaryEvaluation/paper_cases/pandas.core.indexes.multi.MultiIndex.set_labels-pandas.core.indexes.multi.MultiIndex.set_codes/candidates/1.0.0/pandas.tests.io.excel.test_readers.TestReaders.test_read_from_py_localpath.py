@td.skip_if_no('py.path')
@td.check_file_leaks
def test_read_from_py_localpath(self, read_ext):
    from py.path import local as LocalPath
    str_path = os.path.join('test1' + read_ext)
    expected = pd.read_excel(str_path, 'Sheet1', index_col=0)
    path_obj = LocalPath().join('test1' + read_ext)
    actual = pd.read_excel(path_obj, 'Sheet1', index_col=0)
    tm.assert_frame_equal(expected, actual)