def test_read_from_pathlib_path(self, setup_path):
    expected = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    with ensure_clean_path(setup_path) as filename:
        path_obj = Path(filename)
        expected.to_hdf(path_obj, 'df', mode='a')
        actual = read_hdf(path_obj, 'df')
    tm.assert_frame_equal(expected, actual)