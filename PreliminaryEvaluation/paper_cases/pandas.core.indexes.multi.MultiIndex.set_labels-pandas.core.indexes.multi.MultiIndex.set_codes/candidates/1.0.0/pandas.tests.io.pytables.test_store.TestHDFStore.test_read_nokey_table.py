def test_read_nokey_table(self, setup_path):
    df = DataFrame({'i': range(5), 'c': Series(list('abacd'), dtype='category')})
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', mode='a', format='table')
        reread = read_hdf(path)
        tm.assert_frame_equal(df, reread)
        df.to_hdf(path, 'df2', mode='a', format='table')
        with pytest.raises(ValueError):
            read_hdf(path)