def test_round_trip_equals(self, setup_path):
    df = DataFrame({'B': [1, 2], 'A': ['x', 'y']})
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', format='table')
        other = read_hdf(path, 'df')
        tm.assert_frame_equal(df, other)
        assert df.equals(other)
        assert other.equals(df)