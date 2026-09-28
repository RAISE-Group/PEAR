def test_read_nokey(self, setup_path):
    df = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', mode='a')
        reread = read_hdf(path)
        tm.assert_frame_equal(df, reread)
        df.to_hdf(path, 'df2', mode='a')
        with pytest.raises(ValueError):
            read_hdf(path)