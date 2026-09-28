@td.skip_if_no('py.path')
def test_read_from_py_localpath(self, setup_path):
    from py.path import local as LocalPath
    expected = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    with ensure_clean_path(setup_path) as filename:
        path_obj = LocalPath(filename)
        expected.to_hdf(path_obj, 'df', mode='a')
        actual = read_hdf(path_obj, 'df')
    tm.assert_frame_equal(expected, actual)