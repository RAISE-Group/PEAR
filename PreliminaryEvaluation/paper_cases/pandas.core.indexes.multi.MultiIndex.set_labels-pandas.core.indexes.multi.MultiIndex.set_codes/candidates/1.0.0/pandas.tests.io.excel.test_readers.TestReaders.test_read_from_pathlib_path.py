def test_read_from_pathlib_path(self, read_ext):
    from pathlib import Path
    str_path = 'test1' + read_ext
    expected = pd.read_excel(str_path, 'Sheet1', index_col=0)
    path_obj = Path('test1' + read_ext)
    actual = pd.read_excel(path_obj, 'Sheet1', index_col=0)
    tm.assert_frame_equal(expected, actual)