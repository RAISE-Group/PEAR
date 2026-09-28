def test_duplicate_column_name(self, setup_path):
    df = DataFrame(columns=['a', 'a'], data=[[0, 0]])
    with ensure_clean_path(setup_path) as path:
        with pytest.raises(ValueError):
            df.to_hdf(path, 'df', format='fixed')
        df.to_hdf(path, 'df', format='table')
        other = read_hdf(path, 'df')
        tm.assert_frame_equal(df, other)
        assert df.equals(other)
        assert other.equals(df)